def count_increases(depths: list[int]) -> int:
    input_length = len(depths)
    deltas = [depths[i] - depths[i-1] for i in range(1,input_length)]
    positive_deltas = [delta for delta in deltas if delta > 0]
    return len(positive_deltas)

def parse_input() -> list[int]:
    depths = list()
    input_file = open("day01_input.txt", "r")

    for line in input_file:
        depths.append(int(line))

    return depths

def get_sliding_sums(depths: list[int]):
    input_length = len(depths)
    sliding_sums = [depths[i] + depths[i+1] + depths[i+2] for i in range(0,input_length - 2)]
    print(sliding_sums)
    print(len(sliding_sums))
    return sliding_sums

def main():
    depths = parse_input()
    depth_sliding_sums = get_sliding_sums(depths)
    number_of_increases = count_increases(depth_sliding_sums)
    print(number_of_increases)

if __name__ == "__main__":
    main()
