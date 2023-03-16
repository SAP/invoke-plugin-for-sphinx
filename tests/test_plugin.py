# pylint: disable=missing-function-docstring

"""Tests for infra_basement.invoke.sphinx_extension"""

from __future__ import annotations

from typing import Any

import pytest
from invoke import Task
from pytest_mock import MockerFixture

from invoke_plugin_for_spinx import setup as setup_
from invoke_plugin_for_spinx._plugin import TaskDocumenter

try:
    import importlib.metadata as importlib_metadata  # type:ignore[import]
except ImportError:
    import importlib_metadata


def test_setup(mocker: MockerFixture) -> None:
    assert setup_(mocker.Mock()) == {
        "version": importlib_metadata.version("invoke_plugin_for_spinx"),
        "parallel_read_safe": True,
    }


@pytest.mark.parametrize(
    "member,can_document", [(Task(lambda ctx: None), True), (123, False)]
)
def test_task_documenter_can_document_member(member: Any, can_document: bool) -> None:
    assert (
        TaskDocumenter.can_document_member(member, "foo", False, None) == can_document
    )
