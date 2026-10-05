# obsidian-cheatsheet

Write your exam cheat sheet as Obsidian notes, run `just cheatsheet`, and get a
dense one-page A4 landscape PDF in three columns.

It also includes the [Obsidian LaTeX Suite](https://github.com/artisticat1/obsidian-latex-suite)
snippet config the notes are written with, a reference guide to those
snippets, and `macros.tex`, which defines the same snippets as LaTeX macros so
anything you type in the vault compiles in the PDF.

## Requirements

- [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just)
- [Tectonic](https://tectonic-typesetting.github.io/) to compile the LaTeX
- Optional, for `cheatsheet-watch` (macOS): [Skim](https://skim-app.sourceforge.io/) and [watchexec](https://github.com/watchexec/watchexec)

## Usage

```bash
just setup                      # install dev dependencies
just cheatsheet                 # notes -> cheatsheet/chapters/*.tex -> cheatsheet/main.pdf
just cheatsheet-open            # open the PDF in Skim
just cheatsheet-watch           # rebuild on every note save, Skim open alongside
```

The recipes read the notes from `examples/notes` by default. To point them at
your own vault folder, either set the env var or pass the folder on the command line:

```bash
export CHEATSHEET_NOTES="$HOME/Obsidian/Course/cheatsheets"
just notes="$HOME/Obsidian/Course/cheatsheets" cheatsheet-watch
```

Each note becomes one `cheatsheet/chapters/<slug>.tex` file. They are typeset in
filename order, so put a number at the start of each name (`01 Basics.md`,
`02 Waves.md`).

## Markdown → LaTeX

| Obsidian | LaTeX |
| --- | --- |
| `#` / `##` / `###` | `\section` / `\subsection` / `\subsubsection` |
| `$x$`, `$$x$$` | `$x$`, `\[x\]`, contents verbatim |
| `- item`, `1. item` | `itemize`, `enumerate`, nested by indent |
| `**b**`, `*i*` / `_i_` | `\textbf`, `\emph` |
| `==h==`, `<u>u</u>` | `\underline` |
| `` `code` `` | `\texttt` |
| `> quote` | `key` environment (centred key result) |
| pipe table | `tabular`, bold header, alignment kept |
| `---` on its own line | `\columnbreak` |
| `%%c%%`, `<!--c-->` | dropped |
| `[[note\|alias]]` | alias text |
| `![[fig-name]]` | `\input{figures/fig-name}` (put TikZ in `cheatsheet/figures/`) |
| other `![[embed]]` | dropped |

Text outside maths is escaped for LaTeX, but backslashes are left alone, so a
macro typed in a note, such as `\Sum{a}{b}{c}`, still reaches the PDF as a
macro call.

## LaTeX Suite snippets

- `latex-suite/data.json` is the full plugin config, snippets included. To use
  it, copy it to `<vault>/.obsidian/plugins/obsidian-latex-suite/data.json`
  and reload the plugin.
- `latex-suite/_latex-snippets.md` is a reference guide to every trigger. Put
  it in your vault and open it in a Hover Editor window while you write.
- `cheatsheet/macros.tex` defines the same snippets as LaTeX macros.

## Layout

```text
src/obsidian_cheatsheet/md2tex.py   the converter
cheatsheet/main.tex                 3-column landscape document
cheatsheet/preamble.tex             layout, headings, key/fig environments
cheatsheet/macros.tex               LaTeX Suite snippets as macros
cheatsheet/chapters/                generated, one file per note
cheatsheet/figures/                 TikZ diagrams for ![[fig-*]] embeds
latex-suite/                        Obsidian LaTeX Suite config + guide
examples/notes/                     a sample note
```

## License

[MIT](LICENSE)
