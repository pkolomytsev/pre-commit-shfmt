"""Entry points and all that."""

import os
import subprocess  # noqa: S404
import sys

import importlib_resources


def get_pkg_resource(pkg_name: str, res_relpath: str) -> str:
    """Get a path to the package resource.

    :param pkg_name: the package name
    :param res_relpath: the resource relative path the package root
    :return: a path to the package resource
    """
    with importlib_resources.as_file(
        importlib_resources.files(pkg_name).joinpath(res_relpath),
    ) as pkg_file:
        return str(pkg_file)


def get_self_resource(res_relpath: str) -> str:
    """Get a path to the package resource of this library.

    :param res_relpath: the resource relative path the package root
    :return: a path to the package resource
    """
    return get_pkg_resource("pre_commit_shfmt", res_relpath)


def shfmt(*argv) -> int:
    """Call the installed shfmt.

    :param argv: shfmt command line arguments
    :return: exit code
    """
    bin_path = get_self_resource("bin")
    exec_path = os.path.join(bin_path, "shfmt")
    if sys.platform in {"win32", "cygwin"}:
        exec_path = f"{exec_path}.exe"
    proc = subprocess.run([exec_path, *argv])  # noqa: S603
    return proc.returncode


def entry() -> int:
    """Shfmt entry point.

    :return: exit code (0 - ok, other - error)
    """
    return shfmt(*sys.argv[1:])
