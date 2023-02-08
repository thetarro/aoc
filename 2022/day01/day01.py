from typing import List


def solution() -> None:
  filename: str = "input.txt"

  lines: List[str] = [line for line in open(filename)]
  max_calories: int = 0
  current_calories: List[int] = []

  for line in lines:
    if line == '\n':
      current_value = sum(current_calories)
      if current_value > max_calories:
        max_calories = current_value
      current_calories = []
    else:
      current_calories.append(int(line))

  print("Solution 1: %d" % (max_calories))    

if __name__ == "__main__":
  solution()
