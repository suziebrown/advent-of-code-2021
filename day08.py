from typing import List, Dict, Tuple

PLAIN_TEXT_ENCODINGS = {
    "ABCEFG":   0,
    "CF":       1,
    "ACDEG":    2,
    "ACDFG":    3,
    "BCDF":     4,
    "ABDFG":    5,
    "ABDEFG":   6,
    "ACF":      7,
    "ABCDEFG":  8,
    "ABCDFG":   9
}
CIPHER_TEXT_LETTERS = ["a", "b", "c", "d", "e", "f", "g"]
PLAIN_TEXT_LETTERS = ["A", "B", "C", "D", "E", "F", "G"]
NUMBER_OF_TEST_DIGITS = 4


class TestData:
    def __init__(self, input_list: List[str]):
        self.coded_list = input_list
        self.decoded_digits = []
        self.sort_each_string()

    def decode(self, code: Dict[str, int]):
        self.decoded_digits = [code[string] for string in self.coded_list]

    def sort_each_string(self):
        for (index, string) in enumerate(self.coded_list):
            self.coded_list[index] = "".join(sorted(string))
        

class TrainingData:
    def __init__(self, input_list: List[str]):
        self.coded_list = input_list
        self.cipher = {}
        self.code = {}
        self.letter_counts = {}
        self.sort_each_string()
        self.get_letter_counts()

    def decode(self):
        self.decipher()
        deciphered_list = self.get_deciphered_input()
        decoded_list = [PLAIN_TEXT_ENCODINGS[string] for string in deciphered_list]
        self.code.clear()
        for digit in range(0, 10):
            self.code.update({self.coded_list[digit]: decoded_list[digit]})

    def get_deciphered_input(self) -> List[str]:
        deciphered_list = []
        for string in self.coded_list:
            deciphered_string = string
            for letter in PLAIN_TEXT_LETTERS:
                deciphered_string = deciphered_string.replace(self.cipher[letter], letter)
            deciphered_string = "".join(sorted(deciphered_string))
            deciphered_list.append(deciphered_string)
        return deciphered_list          

    def decipher(self):
        self.decode_1478()
        assert(len(self.code) == 4)
        self.decipher_BEF()
        assert(len(self.cipher) == 3)
        self.decipher_A()
        assert(len(self.cipher) == 4)
        self.decipher_C()
        assert(len(self.cipher) == 5)
        self.decipher_D()
        assert(len(self.cipher) == 6)
        self.decipher_G()
        assert(len(self.cipher) == 7)

    def get_letter_counts(self):
        all_letters = "".join(self.coded_list)
        for letter in CIPHER_TEXT_LETTERS:
            count = all_letters.count(letter)
            self.letter_counts.update({letter: count})
        
    def sort_each_string(self):
        for (index, string) in enumerate(self.coded_list):
            self.coded_list[index] = "".join(sorted(string))

    def decode_1478(self):
        for string in self.coded_list:
            if len(string) == 2:
                self.code.update({1: string})
            elif len(string) == 4:
                self.code.update({4: string})
            elif len(string) == 3:
                self.code.update({7: string})
            elif len(string) == 7:
                self.code.update({8: string})

    def decipher_BEF(self):
        for letter in CIPHER_TEXT_LETTERS:
            if self.letter_counts[letter] == 6:
                self.cipher.update({"B": letter})
            elif self.letter_counts[letter] == 4:
                self.cipher.update({"E": letter})
            elif self.letter_counts[letter] == 9:
                self.cipher.update({"F": letter})

    def decipher_A(self):
        set_containing_A = set(self.code[7]) - set(self.code[1])
        assert(len(set_containing_A) == 1)
        self.cipher.update({"A": list(set_containing_A)[0]})

    def decipher_C(self):
        cipher_F = self.cipher["F"]
        code_1 = self.code[1]
        cipher_C = code_1.replace(cipher_F, "")
        self.cipher.update({"C": cipher_C})

    def decipher_D(self):
        cipher_B = self.cipher["B"]
        cipher_C = self.cipher["C"]
        cipher_F = self.cipher["F"]
        code_4 = self.code[4]
        cipher_D = code_4.replace(cipher_B, "").replace(cipher_C, "").replace(cipher_F, "")
        self.cipher.update({"D": cipher_D})

    def decipher_G(self):
        cipher_letters_so_far = self.cipher.values()
        cipher_G = set(CIPHER_TEXT_LETTERS) - set(cipher_letters_so_far)
        assert(len(cipher_G) == 1)
        cipher_G = list(cipher_G)[0]
        self.cipher.update({"G": cipher_G})


def main():
    (train, test) = parse_input()
    decoded_displays = decode_displays(train, test)
    decoded_displays_int = list(map(intlist_to_int, decoded_displays))
    
    # Part 1
    print("=== Part 1 ===")
    counts_1478 = [count_1478(display) for display in decoded_displays]
    answer = sum(counts_1478)
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = sum(decoded_displays_int)
    print("Answer:", answer)


def decode_displays(train: List[TrainingData], test: List[TestData]) -> List[List[int]]:
    decoded_displays = []
    for index in range(len(test)):
        train[index].decode()
        test[index].decode(train[index].code)
        decoded_displays.append(test[index].decoded_digits)
        
    return decoded_displays


def count_1478(display: List[int]) -> int:
    return display.count(1) + display.count(4) + display.count(7) + display.count(8)
        

def intlist_to_int(intlist: List[int]) -> int:
    return int("".join([str(digit) for digit in intlist]))


def parse_input() -> Tuple[List[TrainingData], List[TestData]]:
    input_file = open("day08_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    train_list = []
    test_list = []
    for line in input_lines:
        split_line = line.split(" | ")
        train_list.append(split_line[0].split())
        test_list.append(split_line[1].split())

    train = [TrainingData(line) for line in train_list]
    test = [TestData(line) for line in test_list]
    return train, test


if __name__ == "__main__":
    main()
