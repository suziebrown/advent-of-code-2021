from typing import List
import utils


VERSION_BITS = 3
TYPE_BITS = 3
INDICATOR_BITS = 1
LITERAL_BLOCK_LENGTH = 5
LENGTH_TYPE_0_BITS = 15
LENGTH_TYPE_1_BITS = 11


class Packet:
    # PROPERTIES
    # version | 3-bit number
    # type | 3-bit number, either 100=literal or some other value indicating operator type
    # start | position in full input string at which the packet starts
    # end | position in full input string of the final digit of the packet
    # [WIP] parent | the packet directly containing this one if applicable, else None
    
    def __init__(self, input_string: str, start_position: int):
        self.version = input_string[start_position: start_position + VERSION_BITS]
        self.type = input_string[start_position + VERSION_BITS: start_position + VERSION_BITS + TYPE_BITS]
        self.start = start_position
        self.end = None


class Literal(Packet):
    # PROPERTIES
    # value | the literal integer value encoded by the packet
    
    def __init__(self, input_string: str, start_position: int):
        super().__init__(input_string, start_position)
        self.get_value_and_end(input_string)

    def get_value_and_end(self, input_string: str):
        value_bits = ""
        block_start = self.start + VERSION_BITS + TYPE_BITS
        stop_reading = False
        while not stop_reading:
            block = input_string[block_start: block_start + LITERAL_BLOCK_LENGTH]
            if block[0] == "0":
                stop_reading = True
            value_bits += block[1:]
            block_start += LITERAL_BLOCK_LENGTH    
        self.value = int(value_bits, 2)
        self.get_end_position(block_start + 1)

    def get_end_position(self, content_end: int):
        # End of packet is padded with zeros up to a length that is a multiple of four
        content_length = content_end - self.start
        padding_length = (4 - (content_length % 4)) % 4
        self.end = content_end + padding_length
        

class Operator(Packet):
    # PROPERTIES
    # length_type | 1 bit. 0 if subpacket_length = number of bits in subpackets. 1 if subpacket_length = number of direct subpackets.
    # subpacket_length | as explained above
    # subpacket_start_position | position in original input string where subpackets start
    # [WIP] subpackets | list of Packets that are directly contained in this one

    def __init__(self, input_string: str, start_position: int):
        super().__init__(input_string, start_position)
        self.length_type = input_string[start_position + VERSION_BITS + TYPE_BITS]
        self.get_subpacket_length_and_start_position(input_string, start_position + VERSION_BITS + TYPE_BITS + INDICATOR_BITS)
        self.get_subpackets()

    def get_subpacket_length_and_start_position(self, input_string: str, start: int):
        if self.length_type == "0":
            length_string = input_string[start: start + LENGTH_TYPE_0_BITS]
            self.subpacket_start_position = start + LENGTH_TYPE_0_BITS
        elif self.length_type == "1":
            length_string = input_string[start: start + LENGTH_TYPE_1_BITS]
            self.subpacket_start_position = start + LENGTH_TYPE_1_BITS
        self.subpacket_length = int(length_string, 2)

    def get_subpackets(self):
        pass


def main():
    input_bits = parse_input()

    # Test
    print("Testing literal packet D2FE28")
    pkt = Literal(utils.hex_to_binary("D2FE28"), 0)
    print("version:", pkt.version, "type:", pkt.type, "value:", pkt.value, "start:", pkt.start, "end:", pkt.end)
    # parsing of literals is working :D
    print("Testing operator packet 38006F45291200")
    pkt = Operator(utils.hex_to_binary("38006F45291200"), 0)
    print("version:", pkt.version, "type:", pkt.type, "subpacket length:", pkt.subpacket_length, "start:", pkt.start, "end:", pkt.end)
    print("Testing operator packet EE00D40C823060")
    pkt = Operator(utils.hex_to_binary("EE00D40C823060"), 0)
    print("version:", pkt.version, "type:", pkt.type, "subpacket length:", pkt.subpacket_length, "start:", pkt.start, "end:", pkt.end)
    # parsing of operators is working so far as I've implemented it :)
    
    # Part 1
    print("=== Part 1 ===")
    answer = "?"
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = "?"
    print("Answer:", answer)


def parse_input() -> List[str]:
    input_file = open("day16_input.txt", "r")
    input_hex = input_file.read().strip()
    input_file.close()

    input_bits = utils.hex_to_binary(input_hex)
    return input_bits


if __name__ == "__main__":
    main()
