import sys
import threading
from typing import List
import utils


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.is_small = self.is_small_cave()
        self.neighbours_names = []

    def is_small_cave(self) -> bool:
        return not self.name == self.name.upper()

    def add_neighbours(self, neighbours_names: List[str]):
        for name in neighbours_names:
            self.neighbours_names.append(name)


def get_paths(start: Cave, end: Cave, caves: dict[str, Cave]) -> int:
    global count
    count = 0
    get_paths_recursion(start, end, [], caves)
    return count


def get_paths_recursion(start: Cave, end: Cave, small_caves_visited: List[str], caves: dict[str, Cave]):
    global count
    if start.is_small:
        small_caves_visited.append(start.name)
        
    for name in start.neighbours_names:
        neighbour = caves[name]
        if neighbour.name in small_caves_visited:
                continue

        if name == end.name:
            count += 1
        else:
            get_paths_recursion(neighbour, end, small_caves_visited[::], caves)


def get_paths_2(start: Cave, end: Cave, caves: dict[str, Cave]) -> int:
    global count
    count = 0
    get_paths_recursion_2(start, end, [], caves)
    return count


def get_paths_recursion_2(start: Cave, end: Cave, small_caves_visited: List[str], caves: dict[str, Cave]):
    global count
    if start.is_small:
        small_caves_visited.append(start.name)
        
    for name in start.neighbours_names:
        neighbour = caves[name]
        if neighbour.name in small_caves_visited:
            has_revisited = not len(utils.unique(small_caves_visited)) == len(small_caves_visited)
            is_invalid_step = has_revisited or neighbour.name == "start" or neighbour.name == "end"
            if is_invalid_step:
                continue

        if name == end.name:
            count += 1
        else:
            get_paths_recursion_2(neighbour, end, small_caves_visited[::], caves)
                
            
def main():
    input_lines = parse_input()
    caves = get_caves(input_lines)
    
    # Part 1
    print("=== Part 1 ===")
    answer = get_paths(caves["start"], caves["end"], caves)
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = get_paths_2(caves["start"], caves["end"], caves)
    print("Answer:", answer)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def parse_input() -> List[List[str]]:
    input_file = open("day12_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    pairs = [line.split("-") for line in input_lines]
    return pairs


def get_caves(pairs: List[List[str]]) -> dict[str, Cave]:
    caves = dict[str, Cave]()
    all_cave_names = utils.unique(utils.flatten(pairs))
    
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


if __name__ == "__main__":
    main()
