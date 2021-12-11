import math
from typing import List


def mean(values: List[int]) -> float:
    number_of_values = len(values)
    return sum(values) / number_of_values


def median_rounded_down(values: List[int]) -> int:
    number_of_values = len(values)
    middle_position_floor = math.floor(number_of_values / 2) - 1
    values.sort()
    if number_of_values % 2 == 0:
        return math.floor((values[middle_position_floor] + values[middle_position_floor + 1]) / 2)
    else:
        return values[middle_position_floor]
    

def fuel_used_linear(positions: List[int], target: int):
    fuel_per_sub = map(lambda p: abs(p - target), positions)
    return sum(fuel_per_sub)


def fuel_used_quadratic(positions: List[int], target: int) -> int:
    fuel_per_sub = map(lambda p: triangle_number(abs(p - target)), positions)
    return int(sum(fuel_per_sub))


def triangle_number(n: int):
    return n * (n + 1) / 2


def main():
    positions = parse_input()
    
    # Part 1
    print("=== Part 1 ===")
    answer = fuel_used_linear(positions, median_rounded_down(positions))
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer_rounding_down = fuel_used_quadratic(positions, math.floor(mean(positions)))
    answer_rounding_up = fuel_used_quadratic(positions, math.ceil(mean(positions)))
    answer = min(answer_rounding_up, answer_rounding_down)
    print("Answer:", answer)


def parse_input() -> List[int]:
    input_file = open("day07_input.txt", "r")
    inputs = input_file.read().strip().split(",")
    input_file.close()
    positions = list(map(int, inputs))
    return positions


if __name__ == "__main__":
    main()
