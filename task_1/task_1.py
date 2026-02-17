from __future__ import annotations

from pathlib import Path


def total_salary(path: str) -> tuple[float, float]:
    total = 0.0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue

                try:
                    _, salary_text = line.split(",", 1)
                    total += float(salary_text)
                    count += 1
                except ValueError:
                    continue
    except OSError:
        return 0.0, 0.0

    average = total / count if count else 0.0
    return total, average


if __name__ == "__main__":
    data_file = Path(__file__).with_name("salary_data.txt")
    total_value, average_value = total_salary(str(data_file))
    assert total_value == 6000.0
    assert average_value == 2000.0
    assert total_salary("missing_file.txt") == (0.0, 0.0)
    print("task_1: all asserts passed")
