from typing import List, Optional
import math


SCORE_1_LOOKUP = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
SCORE_2_LOOKUP = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


class Sequence:
    def __init__(self, string: str):
        self.string = string
        self.first_error_position = None
        self.first_error_character = None
        self.stack = []

    def get_score_1(self) -> int:
        if self.first_error_position is None:
            return 0
        else:
            assert(is_closer(self.first_error_character))
            return SCORE_1_LOOKUP[self.first_error_character]

    def get_score_2(self) -> Optional[int]:
        if self.first_error_position is not None:
            return None
        else:
            score = 0
            while len(self.stack) > 0:
                next_opener = self.top_of_stack()
                score = update_score_2(score, next_opener)
                self.stack.pop()
            return score

    def find_first_error(self):
        for index, character in enumerate(self.string):
            push_successful = self.push_or_error(character)
            if not push_successful:
                self.first_error_position = index
                self.first_error_character = character
                return

    def push_or_error(self, character: str) -> bool:
        if is_closer(character):
            if is_valid_pair(self.top_of_stack(), character):
                self.stack.pop()
                return True
            else:
                return False
        elif is_opener(character):
            self.stack.append(character)
            return True
        else:
            raise Exception("Argument was not a valid opening or closing delimiter")

    def top_of_stack(self) -> str:
        return self.stack[len(self.stack) - 1]
    

def is_opener(character: str) -> bool:
    return character in ["<", "(", "[", "{"]


def is_closer(character: str) -> bool:
    return character in [">", ")", "]", "}"]


def is_valid_pair(opener: str, closer: str) -> bool:
    if opener == "<":
        return closer == ">"
    elif opener == "(":
        return closer == ")"
    elif opener == "[":
        return closer == "]"
    elif opener == "{":
        return closer == "}"
    else:
        raise Exception("First argument was not a valid opening delimiter")


def update_score_2(current_score: int, next_opener: str) -> int:
    assert(is_opener(next_opener))
    new_score = current_score * 5 + SCORE_2_LOOKUP[next_opener]
    return new_score


def median(values: List[int]) -> int:
    number_of_values = len(values)
    middle_position = math.floor(number_of_values / 2) 
    values.sort()
    return values[middle_position]
    

def main():
    sequences = parse_input()
    for sequence in sequences:
        sequence.find_first_error()
    
    # Part 1
    print("=== Part 1 ===")
    scores = [sequence.get_score_1() for sequence in sequences]
    answer = sum(scores)
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    scores = [sequence.get_score_2() for sequence in sequences]
    scores_not_none = [score for score in scores if score is not None]
    answer = median(scores_not_none)
    print("Answer:", answer)


def parse_input() -> List[Sequence]:
    input_file = open("day10_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    sequences = [Sequence(line) for line in input_lines]
    return sequences


if __name__ == "__main__":
    main()
