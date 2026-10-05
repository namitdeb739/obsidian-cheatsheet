# Folder of Obsidian notes to typeset; override with CHEATSHEET_NOTES or `just notes=... <recipe>`
notes := env("CHEATSHEET_NOTES", "examples/notes")

# List available recipes
default:
    @just --list

# Install dependencies
setup:
    uv sync --dev

# Convert the Obsidian cheat-sheet notes into cheatsheet/chapters/
cheatsheet-sync:
    uv run python -m obsidian_cheatsheet.md2tex --notes "{{ notes }}"

# Build the one-page LaTeX cheat sheet from the Obsidian notes
cheatsheet: cheatsheet-sync
    tectonic -X compile cheatsheet/main.tex --outdir cheatsheet --synctex

# Open the built cheat sheet in Skim
cheatsheet-open:
    open -a Skim cheatsheet/main.pdf

# Rebuild on every note edit, with Skim open on the PDF
cheatsheet-watch: cheatsheet cheatsheet-open
    watchexec -w "{{ notes }}" -e md -- just notes="{{ notes }}" cheatsheet

# Run all checks
check: lint test

# Lint and check formatting
lint:
    uv run ruff check src/ tests/
    uv run ruff format --check src/ tests/

# Auto-fix lint and formatting issues
fix:
    uv run ruff check --fix src/ tests/
    uv run ruff format src/ tests/

# Run tests
test *args:
    uv run pytest -v {{ args }}
