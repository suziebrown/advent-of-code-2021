from typing import List


HEX_BINARY_LOOKUP = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def hex_to_binary(hex_string: str) -> str:
    bits = ""
    for digit in hex_string:
        bits += HEX_BINARY_LOOKUP[digit]
    return bits

            
def flatten(list_of_lists: List[List]) -> List:
    return [item for sublist in list_of_lists for item in sublist]


def unique(l: List) -> List:
    return list(set(l))


def transpose(array: List[List[str]]) -> List[List[str]]:
    number_of_columns = len(array[0])
    transposed_array = [[row[column_index] for row in array] for column_index in range(number_of_columns)]
    return transposed_array


def invert(bit: str) -> str:
    if bit not in ["0", "1"]:
        raise Exception("Expected a binary digit but got \"" + str(bit) + "\"")
    return "1" if bit == "0" else "0"


def triangle_number(n: int):
    return n * (n + 1) / 2


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

