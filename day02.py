from typing import List


def parse_input() -> List[str]:
    instructions = []
    input_file = open("day02_input.txt", "r")

    for line in input_file:
        instructions.append(line)

    return instructions


def calculate_position(instructions: List[str]) -> tuple[int, int]:
    horizontal = 0
    depth = 0
    for instruction in instructions:
        if instruction[0:8] == "forward ":
            horizontal = horizontal + int(instruction[8])
        elif instruction[0:3] == "up ":
            depth = depth - int(instruction[3])
        elif instruction[0:5] == "down ":
            depth = depth + int(instruction[5])
        else:
            print("Unexpected instruction type")
    return (horizontal, depth)


def calculate_position_2(instructions: List[str]) -> tuple[int, int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        if instruction[0:8] == "forward ":
            instruction_distance = int(instruction[8])
            horizontal = horizontal + instruction_distance
            depth = depth + aim * instruction_distance
        elif instruction[0:3] == "up ":
            aim = aim - int(instruction[3])
        elif instruction[0:5] == "down ":
            aim = aim + int(instruction[5])
        else:
            print("Unexpected instruction type")
    return (horizontal, depth, aim)


def main():
    instructions = parse_input()
    print("the number of instructions is " + str(len(instructions)))

    ## Part 1
    print("=== Part 1 ===")
    (horizontal, depth) = calculate_position(instructions)
    print("the final position is: horizontal=" + str(horizontal) + " depth=" + str(depth))
    print("multiplied together this gives " + str(position[0] * position[1]))

    ## Part 2
    print("=== Part 2 ===")
    (horizontal, depth, aim) = calculate_position_2(instructions)
    print("the final position is: horizontal=" + str(horizontal) + " depth=" + str(depth) + " aim=" + str(aim))
    print("multiplied together this gives " + str(horizontal * depth))


if __name__ == "__main__":
    main()
