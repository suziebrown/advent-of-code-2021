import sys
import threading
from typing import List


GRID_WIDTH = 100
GRID_HEIGHT = 100
MAX_HEIGHT = 9


class Point:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.height = heights[row][column]

    def get_neighbours(self) -> List[Point]:
        neighbours = [] 
        if self.row > 0:
            neighbours.append(Point(self.row - 1, self.column))
        if self.column > 0:
            neighbours.append(Point(self.row, self.column - 1))
        if self.row < GRID_HEIGHT - 1:
            neighbours.append(Point(self.row + 1, self.column))
        if self.column < GRID_WIDTH - 1:
            neighbours.append(Point(self.row, self.column + 1))
        return neighbours

    def is_low_point(self) -> bool:
        adjacent_heights = [p.height for p in self.get_neighbours()]
        return self.height < min(adjacent_heights)


def get_total_risk_level() -> int:
    total_risk = 0
    
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            point = Point(row, column)
            if point.is_low_point():
                total_risk += point.height + 1

    return total_risk


def get_basin_sizes() -> List[int]:
    basin_sizes = []

    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            point = Point(row, column)
            if point.is_low_point():
                basin_sizes.append(get_basin_size(point))

    return basin_sizes


def get_basin_size(low_point: Point) -> int:
    basin = [low_point]
    add_adjacent_points_to_basin(low_point, basin)
    return len(basin)


def add_adjacent_points_to_basin(current_point: Point, basin: List[Point]):
    neighbours = current_point.get_neighbours()
    for point in neighbours:
        if point.height < MAX_HEIGHT and not already_added(point, basin):
            basin.append(point)
            add_adjacent_points_to_basin(point, basin)


def already_added(new_point: Point, list_of_points: List[Point]) -> bool:
    for p in list_of_points:
        if p.row == new_point.row and p.column == new_point.column:
            return True
    return False


def parse_input() -> List[List[int]]:
    input_file = open("day09_input.txt", "r")
    input_rows = input_file.read().strip().split("\n")
    input_file.close()

    rows = [list(row) for row in input_rows]  
    heights = [list(map(int, row)) for row in rows]
    return heights


def main():
    global heights
    heights = parse_input()
    
    # Part 1
    print("=== Part 1 ===")
    answer = get_total_risk_level()
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    basin_sizes = get_basin_sizes()
    basin_sizes.sort(reverse = True)
    answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print("Answer:", answer)
    

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


if __name__ == "__main__":
    main()

