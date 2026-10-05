"""Tests for obsidian_cheatsheet.md2tex."""

from __future__ import annotations

from typing import TYPE_CHECKING

from obsidian_cheatsheet.md2tex import HEADER, convert, sync

if TYPE_CHECKING:
    from pathlib import Path


def test_maths_passes_through_verbatim() -> None:
    assert convert("a $x_1 & y$ b") == "a $x_1 & y$ b\n"
    assert convert("$$\\frac{a}{b}$$") == "\\[\\frac{a}{b}\\]\n"


def test_text_is_escaped_but_backslash_kept() -> None:
    assert convert("50% & \\Sum{a}{b}{c}") == "50\\% \\& \\Sum{a}{b}{c}\n"


def test_headings_quote_and_column_break() -> None:
    out = convert("# A\n## B\n> key\n\n---\n")
    assert "\\section{A}" in out
    assert "\\subsection{B}" in out
    assert "\\begin{key}\nkey\n\\end{key}" in out
    assert "\\columnbreak" in out


def test_comments_and_frontmatter_dropped() -> None:
    assert convert("---\ntags: [x]\n---\nkeep %%drop%%") == "keep\n"


def test_sync_writes_chapters_in_filename_order(tmp_path: Path) -> None:
    notes, out = tmp_path / "notes", tmp_path / "chapters"
    notes.mkdir()
    (notes / "02 Second.md").write_text("two")
    (notes / "01 First.md").write_text("one")

    written = sync(notes, out)

    assert [p.name for p in written] == ["01-first.tex", "02-second.tex"]
    manifest = (out / "all.tex").read_text()
    assert manifest.startswith(HEADER)
    assert manifest.index("01-first") < manifest.index("02-second")
