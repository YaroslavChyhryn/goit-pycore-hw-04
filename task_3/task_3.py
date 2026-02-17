from __future__ import annotations

import sys
from pathlib import Path

try:
    from colorama import Fore, Style, init
except ImportError:  # Fallback when colorama is not installed.
    class _Fallback:
        RESET_ALL = ""
        BLUE = ""
        GREEN = ""

    Fore = _Fallback()
    Style = _Fallback()

    def init(*args, **kwargs):
        return None


def build_tree_entries(directory: Path, prefix: str = "") -> list[tuple[str, bool]]:
    lines: list[tuple[str, bool]] = []
    entries = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        lines.append((f"{prefix}{connector}{entry.name}", entry.is_dir()))

        if entry.is_dir():
            next_prefix = prefix + ("    " if is_last else "│   ")
            lines.extend(build_tree_entries(entry, next_prefix))

    return lines


def print_tree(directory_path: str) -> None:
    path = Path(directory_path)
    if not path.exists():
        print("Error: path does not exist.")
        return
    if not path.is_dir():
        print("Error: path is not a directory.")
        return

    init(autoreset=True)
    print(f"{Fore.BLUE}{path.name}{Style.RESET_ALL}")

    for line, is_dir in build_tree_entries(path):
        color = Fore.BLUE if is_dir else Fore.GREEN
        print(f"{color}{line}{Style.RESET_ALL}")


def _self_check() -> None:
    root = Path(__file__).with_name("picture")
    lines = build_tree_entries(root)
    text = "\n".join(line for line, _ in lines)
    assert "Logo" in text
    assert "ibm.svg" in text
    assert "bot-icon.png" in text
    print("task_3: all asserts passed")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_tree(sys.argv[1])
    else:
        _self_check()
        print_tree(str(Path(__file__).with_name("picture")))
