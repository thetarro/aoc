from __future__ import annotations

from typing import Sequence, Tuple


from dataclasses import dataclass


@dataclass
class Interval:
    left: int
    right: int

    def contains(self, other: Interval) -> bool:
        return self.left <= other.left <= other.right <= self.right

    def overlaps(self, other: Interval) -> bool:
        return (self.left <= other.right <= self.right) or (
            other.left <= self.right <= other.right
        )


def first_solution(lines: Sequence[str]) -> int:
    return sum(
        1
        for line in lines
        for a, b in [line.split(",")]
        if Interval(*map(int, a.split("-"))).contains(Interval(*map(int, b.split("-"))))
        or Interval(*map(int, b.split("-"))).contains(Interval(*map(int, a.split("-"))))
    )


def second_solution(lines: Sequence[str]) -> int:
    return sum(
        1
        for line in lines
        for a, b in [line.split(",")]
        if Interval(*map(int, a.split("-"))).overlaps(Interval(*map(int, b.split("-"))))
    )


def first_solution_old(lines: Sequence[str]) -> int:
    total_contained = 0
    for line in lines:
        left_interval, right_interval = line.split(",")

        first_interval = Interval(*map(int, left_interval.split("-")))
        second_interval = Interval(*map(int, right_interval.split("-")))

        if first_interval.contains(second_interval) or second_interval.contains(
            first_interval
        ):
            total_contained += 1

    return total_contained


def second_solution_old(lines: Sequence[str]) -> int:
    total_overlapping = 0
    for line in lines:
        left_interval, right_interval = line.split(",")

        first_interval = Interval(*map(int, left_interval.split("-")))
        second_interval = Interval(*map(int, right_interval.split("-")))

        if first_interval.overlaps(second_interval):
            total_overlapping += 1

    return total_overlapping


if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    assert Interval(2, 5).contains(Interval(2, 3)) == True
    assert Interval(2, 5).contains(Interval(1, 3)) == False
    assert Interval(2, 5).contains(Interval(3, 4)) == True
    assert Interval(2, 5).contains(Interval(3, 6)) == False
    assert Interval(2, 5).contains(Interval(1, 9)) == False
    assert Interval(2, 5).contains(Interval(2, 5)) == True

    assert Interval(2, 5).overlaps(Interval(2, 3)) == True
    assert Interval(2, 5).overlaps(Interval(1, 3)) == True
    assert Interval(2, 5).overlaps(Interval(3, 4)) == True
    assert Interval(2, 5).overlaps(Interval(3, 6)) == True
    assert Interval(2, 5).overlaps(Interval(1, 9)) == True
    assert Interval(2, 5).overlaps(Interval(2, 5)) == True
    assert Interval(2, 5).overlaps(Interval(6, 9)) == False
    assert Interval(2, 5).overlaps(Interval(0, 1)) == False
    assert Interval(2, 5).overlaps(Interval(10, 12)) == False
    assert Interval(2, 5).overlaps(Interval(6, 7)) == False

    first_value = first_solution(lines)
    print("Solution 1: %d" % (first_value))
    assert first_value == 605

    second_value = second_solution(lines)
    print("Solution 2: %d" % (second_value))
    assert second_value == 914
