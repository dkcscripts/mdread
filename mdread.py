#!/usr/bin/env python3
"""mdread — render markdown files beautifully in the terminal (powered by rich)."""

import sys
import argparse
from pathlib import Path

from rich.console import Console, ConsoleOptions
from rich.markdown import Markdown, CodeBlock
from rich.syntax import Syntax
from rich.rule import Rule


# --- patch CodeBlock to add line numbers ---
def _code_block_with_linenos(self, console: Console, options: ConsoleOptions):
    code = str(self.text).rstrip()
    syntax = Syntax(
        code,
        self.lexer_name,
        theme=self.theme,
        line_numbers=True,
        word_wrap=True,
        padding=1,
    )
    yield syntax

CodeBlock.__rich_console__ = _code_block_with_linenos
# -------------------------------------------


def render(console: Console, source: str) -> None:
    """Read and render one source (path or '-' for stdin)."""
    if source == "-":
        content = sys.stdin.read()
        label = "stdin"
    else:
        path = Path(source)
        if not path.exists():
            console.print(f"[bold red]Error:[/bold red] not found: {source}")
            return
        content = path.read_text(encoding="utf-8")
        label = source

    console.print(Rule(f"[bold cyan]{label}[/bold cyan]", style="bright_black"))
    console.print(Markdown(content, code_theme="monokai"))
    console.print()


def main() -> None:
    # Force UTF-8 on Windows to handle box-drawing / block chars
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        prog="mdread",
        description="Render markdown file(s) in the terminal.",
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="Markdown file(s) to render. Pass - to read from stdin.",
    )
    args = parser.parse_args()

    console = Console(legacy_windows=False)

    if not args.files:
        if not sys.stdin.isatty():
            render(console, "-")
        else:
            parser.print_help()
            sys.exit(1)
    else:
        for f in args.files:
            render(console, f)


if __name__ == "__main__":
    main()
