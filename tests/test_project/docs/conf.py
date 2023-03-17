# pylint: disable=invalid-name
"""Sphinx configuration."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Test Project"
version = release = "1.0.0"
extensions = ["sphinx.ext.autodoc", "invoke_plugin_for_sphinx"]
