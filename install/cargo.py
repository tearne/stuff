#!/usr/bin/env python3
import util
import os
import subprocess
import re


def main():
    install_cargo()
    # install_cargo_packages("cargo-deb")


def install_cargo():
    if util.run("cargo -V") == 0:
        print("Cargo is already installed")
        return

    util.run("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y")
    # Update the path used by this Python process to include newly installed `cargo`
    pattern = "^PATH=(.*?)\\n$"
    string = subprocess.run(""". "$HOME/.cargo/env" && env | grep PATH""", shell=True, stdout=subprocess.PIPE, encoding='utf8').stdout
    match = re.search(pattern, string)
    os.environ["PATH"] = match.group(1)


def install_cargo_packages(*packages):
    for p in packages:
        print(f" *** installing cargo package {p}")
        util.run(f"cargo install {p}")


if __name__ == "__main__":
    main(util.Password())
