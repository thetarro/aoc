from dataclasses import dataclass
from enum import Enum
from typing import List, Sequence, Tuple, TypeVar


class NodeType(Enum):
    UNKNOWN = -1
    FILE = 1
    DIRECTORY = 2


Node = TypeVar("Node")


@dataclass
class Node:
    name: str
    type: NodeType
    parent: Node
    children: dict[str, Node]
    size: int


def parse_tree(lines: Sequence[str]) -> Node:
    current_directory = None
    root_directory = None
    for line in lines:
        if line[0] == "$":  # command
            command, *args = line[2:].split(" ")
            if command == "cd":  # change directory
                dir_name = args[0]
                if dir_name == "..":  # go up one level
                    current_directory = current_directory.parent
                else:  # go down one level
                    child_directory = Node(
                        name=dir_name,
                        type=NodeType.DIRECTORY,
                        parent=current_directory,
                        children={},
                        size=0,
                    )
                    if current_directory == None:
                        current_directory = root_directory = child_directory
                    elif dir_name not in current_directory.children:
                        current_directory.children[dir_name] = child_directory
                    current_directory = child_directory

            if command == "ls":  # list files in directory
                pass
        elif line[:3] == "dir":  # directory details
            pass
        else:  # file details
            filesize, filename = line.split()
            filenode = Node(
                name=filename,
                type=NodeType.FILE,
                parent=current_directory,
                children={},
                size=int(filesize),
            )
            if filename not in current_directory.children:
                current_directory.children[filename] = filenode
    return root_directory


def compute_node_size(root: Node) -> None:
    compute_node_size_helper(root)


def compute_node_size_helper(node: Node) -> int:
    if node.type == NodeType.FILE:
        return node.size
    node_size = 0
    for child in node.children.values():
        node_size += compute_node_size_helper(child)
    node.size = node_size
    return node_size


def compute_total_sum(root: Node, size_limit: int) -> int:
    queue: list[Node] = []
    queue.append(root)
    total_size = 0
    while len(queue) > 0:
        current_node = queue.pop()
        if current_node.type is NodeType.DIRECTORY and current_node.size <= size_limit:
            total_size += current_node.size
        for child in current_node.children.values():
            queue.append(child)
    return total_size


def first_solution(lines: Sequence[str]) -> int:
    root = parse_tree(lines)
    compute_node_size(root)
    return compute_total_sum(root, 100000)


def second_solution(lines: Sequence[str]) -> int:
    total_space = 70_000_000
    free_space_needed = 30_000_000
    root = parse_tree(lines)
    compute_node_size(root)

    if root.size + free_space_needed < total_space:
        # enough free space already, nothing to delete
        return -1
  
    minumum_space_to_delete = root.size + free_space_needed - total_space 

    queue: List[Node] = []
    directory_sizes: List[int] = []
    queue.append(root)
    while len(queue) > 0:
        current_node = queue.pop()
        if current_node.type is NodeType.DIRECTORY:
            directory_sizes.append(current_node.size)
        for child in current_node.children.values():
            queue.append(child)

    directory_sizes.sort()
    for size in directory_sizes:
        if size > minumum_space_to_delete:
            return size
    return -1

if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in open("input.txt")]

    first_value = first_solution(lines)
    print(f"Solution 1: {first_value}")
    assert first_value == 1447046

    second_value = second_solution(lines)
    print(f"Solution 2: {second_value}")
    assert second_value == 578710
