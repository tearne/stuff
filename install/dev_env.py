#!/usr/bin/python3

###
# Test me in a container with something like 
# docker run -it --rm -v $(pwd):/vol ubuntu bash
###

import subprocess
import sys
import os
import importlib
import site
import tempfile
import shutil
import re


def main():
    global pexpect
    global getpass
    pexpect = ensure_import("pexpect")
    getpass = ensure_import("getpass")

    password = Password()

    sudo("apt update", password, 60)
    sudo("""apt install -y curl wget python3-pip""", password, 60)

    install_cargo()
    install_cargo_packages("cargo-deb")

    py_version = "3.11.2"
    compile_and_install_python(py_version, password)
    ensure_venv(py_version, 
        "GitPython",
        "boto3",
        "dpath",
        "lxml",
        "polars",
        "seaborn",
        "pyarrow",
        "pandas"
    )

def ensure_venv(version, *libs):
    ver_minor='.'.join(version.split('.')[0:2])
    run(f"python{ver_minor} -m venv .env")

    run(f""". .env/bin/activate && pip{ver_minor} install {" ".join(libs)}""")


def compile_and_install_python(version, password, del_tmp=True):
    ver_minor='.'.join(version.split('.')[0:2])

    if run(f"python{ver_minor} --version") == 0:
        print(f"Python version {ver_minor} is already installed")
        return
    else:
        print(f"Python version {ver_minor} not installed yet")

    sudo(
        "DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev",
        password,
        60
    )
    
    tempdir = tempfile.mkdtemp(prefix="build-")
    print("* Build in ",tempdir)

    run(
        f"wget -c https://www.python.org/ftp/python/{version}/Python-{version}.tar.xz  -O - | tar -Jx",
        tempdir
    )

    py_dir = f"{tempdir}/Python-{version}"
    sudo(
        "./configure --enable-optimizations",
        password,
        -1,
        cwd=py_dir
    )    
    sudo(
        "make altinstall",
        password,
        1200,
        cwd=py_dir
    )

    if del_tmp:
        sudo(
            f"rm -rf {tempdir}",
            password,
            5
        )

def install_cargo():
    if run(f"cargo -V") == 0:
        print(f"Cargo is already installed")
        return

    run("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y")
    # Update the path used by this Python process to include newly installed `cargo`
    pattern="^PATH=(.*?)\\n$"
    string = subprocess.run(""". "$HOME/.cargo/env" && env | grep PATH""", shell=True, stdout=subprocess.PIPE, encoding='utf8').stdout
    match = re.search(pattern, string)
    os.environ["PATH"] = match.group(1)

def install_cargo_packages(*packages):
    for p in packages:
        print(f" *** installing cargo package {p}")
        run(f"cargo install {p}")

#
# utils below
#
class Password:
    def __init__(self):
        self.p = None

    def get(self):
        if self.p: return self.p
        else:
            self.p = getpass.getpass()
            return self.p

def run(cmd, cwd=None):
    print(" *** Running:", cmd)
    return subprocess.run(
        cmd,
        shell=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
        encoding='utf8',
        cwd=cwd
    ).returncode

def is_already_root():
    return os.geteuid() == 0

def sudo(cmd, password, timeout = -1, cwd=None):
    if is_already_root():
        run(cmd, cwd)
    else:
        command = f"sudo {cmd}"
        print(" *** Running (sudo): ", cmd)
        child = pexpect.spawnu(command, cwd=cwd)
        child.logfile_read=sys.stdout
        options = ['password', pexpect.TIMEOUT, pexpect.EOF]
        index = child.expect(options, timeout = 1)
        if index > 0:
            print(f"Error waiting for password prompt: {options[index]} - {child.before.decode()}")
            sys.exit(1)
        
        child.sendline(password.get())
        
        options = [pexpect.EOF, 'try again', pexpect.TIMEOUT]
        index = child.expect(options, timeout=timeout)
        if index == 0:
            return
        elif index == 1:
            print(f"Authentication failure: {options[index]}")
            sys.exit(1)
        else:
            print(f"Command failure: {options[index]}")
            sys.exit(1)


def ensure_import(package_name):
    try:
        pkg = importlib.import_module(package_name)
        print(f"Dependency '{package_name}' already installed")
        return pkg
    except ImportError as err:
        print(f"Dependency {package_name} not installed yet: {err}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        importlib.reload(site)
        importlib.invalidate_caches()
        return importlib.import_module(package_name)


if __name__ == '__main__':
    main()