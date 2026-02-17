from __future__ import annotations

from pathlib import Path


def get_cats_info(path: str) -> list[dict[str, str]]:
    cats: list[dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})
    except OSError:
        return []

    return cats


if __name__ == "__main__":
    data_file = Path(__file__).with_name("cats_data.txt")
    result = get_cats_info(str(data_file))
    assert result[0] == {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"}
    assert len(result) == 5
    assert get_cats_info("missing_file.txt") == []
    print("task_2: all asserts passed")
