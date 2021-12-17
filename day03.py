from typing import List, Tuple


LENGTH_OF_BINARY_NUMBERS = 12


def parse_input() -> List[str]:
    inputs = list()
    input_file = open("day03_input.txt", "r")

    for line in input_file:
        inputs.append(line)

    input_file.close()
    return inputs


def get_gamma_and_epsilon(gamma_bits: List[str]) -> Tuple[int, int]:
    epsilon_bits = [invert(bit) for bit in gamma_bits]

    gamma = bits_to_decimal(gamma_bits)
    epsilon = bits_to_decimal(epsilon_bits)

    return gamma, epsilon


def get_gamma_bits(inputs: List[str]) -> List[str]:
    gamma_bits = []
    
    for position in range(LENGTH_OF_BINARY_NUMBERS):
        bits_at_position = [binary_number[position] for binary_number in inputs]
        most_common_bit_at_position = get_most_common_bit(bits_at_position)
        gamma_bits.append(most_common_bit_at_position)

    return gamma_bits


def get_oxygen_rating(inputs: List[str]) -> str:
    filtered_inputs = inputs

    for position in range(LENGTH_OF_BINARY_NUMBERS):
        bits_at_position = [binary_number[position] for binary_number in filtered_inputs]
        most_common_bit_at_position = get_most_common_bit_or_default(bits_at_position)
        
        filtered_inputs = [binary_number for binary_number in filtered_inputs if binary_number[position] == most_common_bit_at_position]
        if len(filtered_inputs) == 1:
            return filtered_inputs[0]

    raise Exception("Didn't end up with exactly one entry")

    
def get_co2_rating(inputs: List[str]) -> List[str]:
    filtered_inputs = inputs

    for position in range(LENGTH_OF_BINARY_NUMBERS):
        bits_at_position = [binary_number[position] for binary_number in filtered_inputs]
        least_common_bit_at_position = get_least_common_bit_or_default(bits_at_position)
        
        filtered_inputs = [binary_number for binary_number in filtered_inputs if binary_number[position] == least_common_bit_at_position]
        if len(filtered_inputs) == 1:
            return filtered_inputs[0]

    raise Exception("Didn't end up with exactly one entry")


def get_most_common_bit(inputs: List[str]) -> str:
    number_of_zeros = inputs.count("0")
    number_of_ones = inputs.count("1")
    if number_of_zeros + number_of_ones != len(inputs):
        raise Exception("There may be inputs other than 0/1")
    elif number_of_zeros == number_of_ones:
        raise Exception("0 and 1 are equally common")
    else:
        is_zero_most_common = number_of_zeros > len(inputs) / 2
        most_common_bit = "0" if is_zero_most_common else "1"
        return most_common_bit


def get_most_common_bit_or_default(inputs: List[str]) -> str:
    # defaults to "1" if 0 and 1 are equally common
    number_of_zeros = inputs.count("0")
    number_of_ones = inputs.count("1")
    
    if number_of_zeros + number_of_ones != len(inputs):
        raise Exception("There may be inputs other than 0/1")
    else:
        is_zero_most_common = number_of_zeros > len(inputs) / 2
        most_common_bit = "0" if is_zero_most_common else "1"
        return most_common_bit


def get_least_common_bit_or_default(inputs: List[str]) -> str:
    # defaults to "0" if 0 and 1 are equally common
    most_common_bit = get_most_common_bit_or_default(inputs)
    least_common_bit = "0" if most_common_bit == "1" else "1"

    return least_common_bit


def invert(bit: str) -> str:
    if bit not in ["0", "1"]:
        print("ERROR in invert: input is not a binary digit")
        return "Error"
    else:
        return "1" if bit == "0" else "0"


def bits_to_decimal(bits: List[str]) -> int:
    binary = "".join(bits)
    decimal = int(binary, 2)
    
    return decimal


def main():
    inputs = parse_input()
    print("the number of inputs is", str(len(inputs)))

    # Part 1
    print("=== Part 1 ===")
    gamma_bits = get_gamma_bits(inputs)
    (gamma, epsilon) = get_gamma_and_epsilon(gamma_bits)
    print("gamma:", gamma)
    print("epsilon:", epsilon)
    print("Answer:", int(gamma) * int(epsilon))
    
    # Part 2
    print("=== Part 2 ===")
    oxygen_binary = get_oxygen_rating(inputs)
    oxygen = int(oxygen_binary, 2)
    co2_binary = get_co2_rating(inputs)
    co2 = int(co2_binary, 2)
    print("Oxygen:", oxygen)
    print("CO2:", co2)
    print("Answer:", oxygen * co2)
    

if __name__ == "__main__":
    main()
