from typing import Sequence, TypeVar


T = TypeVar("T")


def grouper(seq: Sequence[T], group_size: int) -> Sequence[Sequence[T]]:
    return [x for x in zip(*(iter(seq),) * group_size)]
