from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class Move:
    value: int
    from_index: int
    to_index: int


Stack = List[str]
_STACK_SIZE: int = 9


def print_stacks(stacks: dict[int, Stack]) -> None:
    for i, stack in stacks.items():
        print(f"{i}: {stack}")


def parse_stack(line: str) -> Stack:
    tokens = [line[4 * i : 4 * (i + 1)].strip() for i in range(int(len(line) / 4) + 1)]
    return [x[1] if len(x) == 3 else "" for x in tokens]


def parse_stacks(lines: List[str]) -> dict[int, Stack]:
    stacks: dict[int, Stack] = dict((i + 1, []) for i in range(_STACK_SIZE))
    for line in lines:
        if len(line) and line[0] == "[":
            values = parse_stack(line)
            for i, v in enumerate(values):
                if len(v) > 0:
                    stacks[i + 1].append(v)

    for stack in stacks.values():
        stack.reverse()

    return stacks


def parse_move(line: str) -> Move:
    tokens = line.strip().split(" ")
    value = int(tokens[1])
    from_index = int(tokens[3])
    to_index = int(tokens[5])
    return Move(value=value, from_index=from_index, to_index=to_index)


def parse_moves(lines: List[str]) -> List[Move]:
    moves = []
    for line in lines:
        if len(line) and line[0] == "m":
            moves.append(parse_move(line))
    return moves


def execute_move(from_stack: Stack, to_stack: Stack, n: int) -> None:
    assert len(from_stack) >= n
    for i in range(n):
        value = from_stack.pop()
        to_stack.append(value)


def execute_move_together(from_stack: Stack, to_stack: Stack, n: int) -> None:
    assert len(from_stack) >= n
    values = from_stack[-n:]
    del from_stack[-n:]
    to_stack.extend(values)


def first_solution(lines: Sequence[str]) -> str:
    moves = parse_moves(lines)
    stacks = parse_stacks(lines)

    for move in moves:
        execute_move(stacks[move.from_index], stacks[move.to_index], move.value)

    return "".join([stacks[i][-1] for i in range(1, _STACK_SIZE + 1)])


def second_solution(lines: Sequence[str]) -> str:
    moves = parse_moves(lines)
    stacks = parse_stacks(lines)

    for move in moves:
        execute_move_together(
            stacks[move.from_index], stacks[move.to_index], move.value
        )

    return "".join([stacks[i][-1] for i in range(1, _STACK_SIZE + 1)])


if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    first_value = first_solution(lines)
    print(f"Solution 1: {first_value}")
    assert first_value == "BZLVHBWQF"

    second_value = second_solution(lines)
    print(f"Solution 2: {second_value}")
    assert second_value == "TDGJQTZSL"
