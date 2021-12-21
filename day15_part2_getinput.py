from typing import List

HORIZONTAL_EXTENSION_FACTOR = 5
VERTICAL_EXTENSION_FACTOR = 5


def main():
    original_input = parse_original_input()
    extended_input = extend(original_input)
    print(len(extended_input), len(extended_input[0]))
    output = ["".join(line) + "\n" for line in extended_input]
    output_file = open("day15_part2_test_input.txt", "w")
    output_file.writelines(output)


def parse_original_input() -> List[str]:
    input_file = open("day15_test_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()
    return input_lines


def extend(input_lines: List[str]) -> List[List[str]]:
    extended_input = []
    for line in input_lines:
        extended_input.append(extend_horizontally(line))

    extended_lines = extended_input
    current_line_index = 0
    for _ in range(1, VERTICAL_EXTENSION_FACTOR):
        for i in range(len(input_lines)):
            line_to_add = list(map(increment_risk, extended_lines[current_line_index]))
            extended_lines.append(line_to_add)
            current_line_index += 1

    return extended_input


def extend_horizontally(line: str) -> List[str]:
    current_values = list(line)
    extended_values = current_values

    for _ in range(1, HORIZONTAL_EXTENSION_FACTOR):
        values_to_add = list(map(increment_risk, current_values))
        extended_values += values_to_add
        current_values = values_to_add

    return extended_values


def increment_risk(current_risk: str) -> str:
    updated_risk = int(current_risk) + 1
    if updated_risk > 9:
        updated_risk = 1
    return str(updated_risk)


if __name__ == "__main__":
    main()
