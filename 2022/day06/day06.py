from typing import Sequence


def has_unique_chars(line: str) -> bool:
    return len(set(x for x in line)) == len(line)


def find_pattern_position(line: str, pattern_length: int) -> int:
    index = pattern_length
    for index in range(len(line) + 1):
        if index < pattern_length:
            continue
        if has_unique_chars(line[index - pattern_length : index]):
            return index
    return 0


def first_solution(line: str) -> int:
    return find_pattern_position(line, 4)


def second_solution(line: str) -> int:
    return find_pattern_position(line, 14)


if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    assert has_unique_chars("") == True
    assert has_unique_chars("abcde") == True
    assert has_unique_chars("abcce") == False
    assert has_unique_chars("a") == True
    assert has_unique_chars("aa") == False

    assert find_pattern_position("abcd", 4) == 4
    assert find_pattern_position("abcde", 4) == 4
    assert find_pattern_position("aabcd", 4) == 5
    assert find_pattern_position("abcbcdbcde", 4) == 10

    first_value = first_solution(lines[0])
    print(f"Solution 1: {first_value}")
    assert first_value == 1238

    second_value = second_solution(lines[0])
    print(f"Solution 2: {second_value}")
    assert second_value == 3037
