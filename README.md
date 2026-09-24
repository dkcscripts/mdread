# mdread

Render markdown files beautifully in the terminal, powered by [rich](https://github.com/Textualize/rich).

## Features

- Headings, bold, italic, links, blockquotes, tables
- Syntax-highlighted code blocks (monokai theme) with line numbers
- Multiple files in one call, each with a labeled separator
- Stdin support via `-`

## Requirements

```
pip install rich
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python mdread.py FILE [FILE ...]
python mdread.py -               # read from stdin
```

### Examples

```bash
python mdread.py README.md
python mdread.py docs/api.md docs/guide.md
cat notes.md | python mdread.py -
```

## Files

```
mdread/
├── mdread.py        # main script
├── mdread.sh        # bash launcher
├── requirements.txt # dependencies
└── README.md        # this file
```
