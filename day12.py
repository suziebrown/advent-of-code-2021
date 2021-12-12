from typing import List


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.is_small = self.is_small_cave()
        self.neighbours_names = []

    def is_small_cave(self) -> bool:
        return self.name == self.name.upper()

    def add_neighbours(self, neighbours_names: List[str]):
        for name in neighbours_names:
            self.neighbours_names.append(name)


def main():
    input_lines = parse_input()
    caves = get_caves(input_lines)
    
    # Test
    
    # Part 1
    print("=== Part 1 ===")
    answer = "?"
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = "?"
    print("Answer:", answer)


def parse_input() -> List[List[str]]:
    input_file = open("day12_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    pairs = [line.split("-") for line in input_lines]
    return pairs


def get_caves(pairs: List[List[str]]) -> List[Cave]:
    caves = dict[str, Cave]()
    all_cave_names = unique(flatten(pairs))
    
    for name in all_cave_names:
        new_cave = Cave(name)
        caves.update({name: new_cave})
        
    for name in all_cave_names:
        neighbours_names = get_neighbours_names(name, pairs)
        caves[name].add_neighbours(neighbours_names)

    return caves


def get_neighbours_names(name_here: str, pairs: List[List[str]]) -> List[str]:
    neighbours = []
    for pair in pairs:
        if pair[0] == name_here:
            neighbours.append(pair[1])
        elif pair[1] == name_here:
            neighbours.append(pair[0])

    return neighbours


def flatten(list_of_lists: List[List]) -> List:
    return [item for sublist in list_of_lists for item in sublist]


def unique(l: List) -> List:
    return list(set(l))


if __name__ == "__main__":
    main()
