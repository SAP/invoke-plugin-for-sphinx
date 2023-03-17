# pylint: disable=missing-function-docstring

"""Tests for infra_basement.invoke.sphinx_extension"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any

import pytest
from invoke import Task
from pytest_mock import MockerFixture

from invoke_plugin_for_sphinx import setup as setup_
from invoke_plugin_for_sphinx._plugin import TaskDocumenter


def test_setup(mocker: MockerFixture) -> None:
    mocker.patch(
        "invoke_plugin_for_sphinx._plugin.importlib_metadata.version",
        return_value="1.0.0",
    )
    assert setup_(mocker.Mock()) == {
        "version": "1.0.0",
        "parallel_read_safe": True,
    }


@pytest.mark.parametrize(
    "member,can_document", [(Task(lambda ctx: None), True), (123, False)]
)
def test_task_documenter_can_document_member(member: Any, can_document: bool) -> None:
    assert (
        TaskDocumenter.can_document_member(member, "foo", False, None) == can_document
    )


def test_render() -> None:
    build_dir = Path("tests/test_project/docs/_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)
    subprocess.run(
        [
            "sphinx-build",
            "-a",
            "-W",
            "tests/test_project/docs/",
            "tests/test_project/docs/_build",
        ],
        check=True,
    )

    index = (build_dir / "index.html").read_text(encoding="utf-8")
    assert "A VERY SPECIAL DOCSTRING." in index
