"""Invoke plugin for sphinx."""

from __future__ import annotations

from importlib.metadata import version
from typing import Any

from invoke.tasks import Task
from sphinx.application import Sphinx
from sphinx.ext.autodoc import FunctionDocumenter
from typing_extensions import override

__all__ = ("TaskDocumenter", "setup")


class TaskDocumenter(FunctionDocumenter):
    """Documenter for :py:class:`invoke.Task`."""

    objtype = "invoketask"
    directivetype = "function"

    @classmethod
    @override
    def can_document_member(
        cls, member: Any, membername: str, isattr: bool, parent: Any
    ) -> bool:
        """Check if the object is an invoke task."""
        return isinstance(member, Task)


def setup(app: Sphinx) -> dict[str, Any]:
    """Setup the extension."""
    our_version = version("invoke_plugin_for_sphinx")
    app.add_autodocumenter(TaskDocumenter)
    return {"version": our_version, "parallel_read_safe": True}
