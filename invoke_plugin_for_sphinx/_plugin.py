"""Invoke plugin for sphinx."""

from __future__ import annotations

from importlib.metadata import version
from typing import Any

import sphinx
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


def _patch_for_sphinx9() -> None:
    # pylint: disable=import-outside-toplevel,protected-access,import-private-name
    from sphinx.ext.autodoc._dynamic import _member_finder

    old_func = _member_finder._best_object_type_for_member

    def _patch(*args: Any, **kwargs: Any) -> Any:  # pragma: no cover
        result = old_func(*args, **kwargs)
        member = args[0] if args else kwargs.get("member")
        return "function" if result is None and isinstance(member, Task) else result

    _member_finder._best_object_type_for_member = _patch


def setup(app: Sphinx) -> dict[str, Any]:
    """Setup the extension."""
    # deprecated with sphinx 9.0, but still works for now
    app.add_autodocumenter(TaskDocumenter)

    if sphinx.version_info[0] >= 9:
        _patch_for_sphinx9()

    return {"version": version("invoke_plugin_for_sphinx"), "parallel_read_safe": True}
