import os
import sys
import getpass
import subprocess

import ensure
ensure.package("pexpect")

import pexpect


class Password:
    def __init__(self):
        self.p = None

    def get(self):
        if self.p:
            return self.p
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


def am_root():
    return os.geteuid() == 0


def sudo(cmd, password, timeout=None, cwd=None):
    if am_root():
        run(cmd, cwd)
    else:
        command = f"sudo {cmd}"
        print(" *** Running (sudo): ", cmd)
        print(f"     Timeout = {timeout}")
        child = pexpect.spawnu(command, cwd=cwd, timeout=timeout)
        child.logfile_read = sys.stdout
        options = ['password', pexpect.TIMEOUT, pexpect.EOF]
        index = child.expect(options, timeout=1)
        if index > 0:
            print(
                f"Error waiting for password prompt:\
                {options[index]} - {child.before.decode()}"
            )
            sys.exit(1)

        child.sendline(password.get())

        options = [pexpect.EOF, 'try again', pexpect.TIMEOUT]
        index = child.expect(options,timeout=timeout)
        if index == 0:
            return
        elif index == 1:
            print(f"Authentication failure: {options[index]}")
            sys.exit(1)
        else:
            print(f"Command failure running: {cmd}\n {options[index]}")
            sys.exit(1)
