from typing import Sequence

WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0

ROCK = "X"
PAPER = "Y"
SCISSORS = "Z"

SCORES: dict[tuple[str, str], int] = dict()
SCORES[("A", "X")] = DRAW_SCORE  # rock, rock
SCORES[("A", "Y")] = WIN_SCORE  # rock, paper
SCORES[("A", "Z")] = LOSS_SCORE  # rock, scissorsS

SCORES[("B", "X")] = LOSS_SCORE  # paper, rock
SCORES[("B", "Y")] = DRAW_SCORE  # paper, paper
SCORES[("B", "Z")] = WIN_SCORE  # paper, scissors

SCORES[("C", "X")] = WIN_SCORE  # scissors, rock
SCORES[("C", "Y")] = LOSS_SCORE  # scissors, paper
SCORES[("C", "Z")] = DRAW_SCORE  # scissors, scissors

PLAY: dict[tuple[str, str], str] = dict()
PLAY[("A", "X")] = SCISSORS  # rock, lose -> scissors
PLAY[("A", "Y")] = ROCK  # rock, draw -> rock
PLAY[("A", "Z")] = PAPER  # rock, win -> paper

PLAY[("B", "X")] = ROCK  # paper, lose -> rock
PLAY[("B", "Y")] = PAPER  # paper, draw -> paper
PLAY[("B", "Z")] = SCISSORS  # paper, win -> scissors

PLAY[("C", "X")] = PAPER  # scissors, lose -> paper
PLAY[("C", "Y")] = SCISSORS  # scissors, draw -> scissors
PLAY[("C", "Z")] = ROCK  # scissors, win -> rock


def get_winning_score(left: str, right: str) -> int:
    key: tuple[str, str] = (left, right)
    return SCORES[key] if key in SCORES else LOSS_SCORE


def get_playable(left: str, right: str) -> str:
    key: tuple[str, str] = (left, right)
    return PLAY[key] if key in PLAY else ""


def get_value_score(value: str) -> int:
    if value == ROCK:
        return 1 
    if value == PAPER:
        return 2
    if value == SCISSORS:
        return 3 
    return 0


def first_solution(lines: Sequence[str]) -> int:
    total_score: int = 0
    for line in lines:
        left, right = line.split(" ")
        total_score += get_winning_score(left, right) + get_value_score(right)
    return total_score


def second_solution(lines: Sequence[str]) -> int:
    total_score: int = 0
    for line in lines:
        left, right = line.split(" ")
        playable: str = get_playable(left, right)
        total_score += get_winning_score(left, playable) + get_value_score(playable)
    return total_score


if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    first_value = first_solution(lines)
    print("Solution 1: %d" % (first_value))
    assert first_value == 12740

    second_value = second_solution(lines)
    print("Solution 2: %d" % (second_value))
    assert second_value == 11980
