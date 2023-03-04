from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class Move:
    value: int
    from_index: int
    to_index: int


def parse_stack(line: str) -> Sequence[str]:
    tokens = [line[4 * i : 4 * (i + 1)].strip() for i in range(int(len(line) / 4))]
    return [x[1] if len(x) == 3 else "" for x in tokens]


def parse_move(line: str) -> Move:
    tokens = line.strip().split(" ")
    value = int(tokens[1])
    from_index = int(tokens[3])
    to_index = int(tokens[5])
    return Move(value=value, from_index=from_index, to_index=to_index)


def first_solution(lines: Sequence[str]) -> int:
    return 0


def second_solution(lines: Sequence[str]) -> int:
    return 0


if __name__ == "__main__":
    STACK_SIZE: int = 9
    lines: list[str] = [line.strip() for line in open("input.txt")]
    stacks: dict[int, list[str]] = dict((i + 1, []) for i in range(STACK_SIZE))

    for line in open("input.txt"):
        if line[0] == "[":
            values = parse_stack(line)
            for i, v in enumerate(values):
                if len(v) > 0:
                    stacks[i + 1].append(v)

        if len(line) == 0:
            continue
        if line[0] == "m":
            move = parse_move(line)
            # print(move)

    for stack in stacks.values():
        stack.reverse()

    for i, stack in stacks.items():
        print(f"{i}: {stack}")

    first_value = first_solution(lines)
    print("Solution 1: %d" % (first_value))
    assert first_value == 0

    second_value = second_solution(lines)
    print("Solution 2: %d" % (second_value))
    assert second_value == 0
