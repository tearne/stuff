import importlib
import subprocess
import sys


def package(package_name):
    try:
        pkg = importlib.import_module(package_name)
        print(f"Dependency '{package_name}' already installed")
        return pkg
    except ImportError as err:
        print(f"Dependency {package_name} not installed yet: {err}")
        subprocess.check_call([
            sys.executable,
            '-m',
            'pip',
            'install',
            package_name
        ])
        # importlib.reload(site)
        importlib.invalidate_caches()
        return importlib.import_module(package_name)
