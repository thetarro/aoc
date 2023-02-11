from functools import reduce
from typing import Sequence, Tuple

ORD_LOWERCASE_A = ord("a")
ORD_LOWERCASE_Z = ord("z")
ORD_UPPERCASE_A = ord("A")
ORD_UPPERCASE_Z = ord("Z")


def divide(s: str) -> Tuple[str, str]:
    n = len(s)
    if n % 2 == 1:
        print("Error on line %s".format(s))
        return ("", "")
    midpoint = int(n / 2)
    return s[:midpoint], s[midpoint:]


def find_common_item(s: str) -> str:
    left, right = divide(s)
    common_set: set[str] = set(left) & set(right)
    if len(common_set) != 1:
        print("Error on line %s".format(s))
        return ""
    return common_set.pop()


def get_priority(s: str) -> int:
    assert len(s) == 1
    value: int = ord(s[0])

    if ORD_LOWERCASE_A <= value <= ORD_LOWERCASE_Z:
        return 1 + value - ORD_LOWERCASE_A
    if ORD_UPPERCASE_A <= value <= ORD_UPPERCASE_Z:
        return 27 + value - ORD_UPPERCASE_A
    return -1


def grouper(seq: Sequence[str], group_size: int) -> Sequence[Sequence[str]]:
    return [x for x in zip(*(iter(seq),) * group_size)]


def first_solution(lines: Sequence[str]) -> int:
    total_value: int = 0
    for line in lines:
        c = find_common_item(line)
        total_value += get_priority(c)

    return total_value


def second_solution(lines: Sequence[str]) -> int:
    total_value: int = 0
    for triplet in grouper(lines, 3):
        common_set : set[str]= reduce(lambda x, y: x & y, (set(t) for t in triplet))
        if len(common_set) != 1:
            print("Error on line %s".format(s))
            return -1
        common_item: str = common_set.pop()
        total_value += get_priority(common_item)

    return total_value


if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    assert divide("abcdef") == ("abc", "def")
    assert divide("aa") == ("a", "a")
    assert divide("abcdefggfedcba") == ("abcdefg", "gfedcba")

    assert find_common_item("abcxya") == "a"
    assert find_common_item("asbcxyzs") == "s"

    assert get_priority("a") == 1
    assert get_priority("c") == 3
    assert get_priority("z") == 26
    assert get_priority("A") == 27
    assert get_priority("E") == 31
    assert get_priority("Z") == 52

    first_value = first_solution(lines)
    print("Solution 1: %d" % (first_value))
    assert first_value == 7553

    second_value = second_solution(lines)
    print("Solution 2: %d" % (second_value))
    assert second_value == 2758
