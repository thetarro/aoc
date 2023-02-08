from typing import List, Tuple


FILENAME: str = "input.txt"

def first_solution() -> None:
  lines: List[str] = [line for line in open(FILENAME)]
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

def second_solution() -> None:
  lines: List[str] = [line for line in open(FILENAME)]
  current_calories: List[int] = []
  elf_calories: List[int] = []

  for line in lines:
    if line == '\n':
      elf_calories.append(sum(current_calories))
      current_calories = []
    else:
      current_calories.append(int(line))
  print("Solution 2: %d" % (sum(sorted(elf_calories, reverse = True)[0:3]))) 

if __name__ == "__main__":
  first_solution()
  second_solution()
