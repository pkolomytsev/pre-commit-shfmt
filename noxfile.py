"""Linting and testing sessions."""

import nox


@nox.session(reuse_venv=True)
def lint(session: nox.Session):
    """Call linting tools.

    :param session: nox session
    """
    session.install(".[lint]")
    session.run("flake8", ".")
    session.run("mypy", ".")


@nox.session()
def test(session: nox.Session):
    """Test an installed shfmt.

    :param session: nox session
    """
    session.install(".")
    session.run("shfmt", "--version")
