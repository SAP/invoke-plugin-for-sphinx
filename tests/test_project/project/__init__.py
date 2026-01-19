"""Tasks."""

from __future__ import annotations

from invoke import task


@task
def dummy(ctx):  # type: ignore[no-untyped-def]
    """A VERY SPECIAL DOCSTRING."""
    ctx.run("echo hello world")
