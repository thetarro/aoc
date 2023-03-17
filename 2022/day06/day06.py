from typing import Sequence

_PATTERN_LENGTH: int = 4


def has_unique_chars(line: str) -> bool:
    return len(set(x for x in line)) == len(line)


def first_solution(line: str) -> int:
    index = _PATTERN_LENGTH
    for index in range(len(line) + 1):
        if index < _PATTERN_LENGTH:
            continue
        if has_unique_chars(line[index - _PATTERN_LENGTH : index]):
            return index
    return 0


def second_solution(line: str) -> int:
    return 0


if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    assert has_unique_chars("") == True
    assert has_unique_chars("abcde") == True
    assert has_unique_chars("abcce") == False
    assert has_unique_chars("a") == True
    assert has_unique_chars("aa") == False

    assert first_solution("abcd") == 4
    assert first_solution("abcde") == 4
    assert first_solution("aabcd") == 5

    first_value = first_solution(lines[0])
    print(f"Solution 1: {first_value}")
    assert first_value == 1238

    second_value = second_solution(lines[0])
    print(f"Solution 2: {second_value}")
    assert second_value == 0
