from typing import List


def main():
    foo = parse_input()
    
    # Part 1
    print("=== Part 1 ===")
    answer = "?"
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = "?"
    print("Answer:", answer)


def parse_input() -> List[str]:
    input_file = open("day12_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()
    return input_lines


if __name__ == "__main__":
    main()
