from typing import List

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

class Training_data:
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
        # TODO: actually want to fill in the rest of self.code (probably clear it first then loop through all)
        decoded_list = [PLAIN_TEXT_ENCODINGS[string] for string in deciphered_list]

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
    # TODO: parse input & calculate the actual answer to the puzzle!

    # Test
    train = Training_data("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb".split())
    train.decode()
    print("Code so far:", train.code)
    print("Cipher:", train.cipher)
    
##    foo = parse_input()
##
##    # Part 1
##    print("=== Part 1 ===")
##    answer = "?"
##    print("Answer:", answer)
##
##    # Part 2
##    print("=== Part 2 ===")
##    answer = "?"
##    print("Answer:", answer)


def parse_input() -> List[int]:
    input_file = open("day08_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()
    # do some other stuff...

    return input_lines


if __name__ == "__main__":
    main()
