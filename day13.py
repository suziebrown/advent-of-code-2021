from typing import List, Tuple


class Fold:
    def __init__(self, direction: str, location: str):
        self.direction = direction
        self.location = int(location)


class Point:
    def __init__(self, x: str, y: str):
        self.x = int(x)
        self.y = int(y)

    def apply_fold(self, fold: Fold):
        if fold.direction == "vertical" and fold.location < self.x:
            self.fold_along_vertical(fold.location)
        elif fold.direction == "horizontal" and fold.location < self.y:
            self.fold_along_horizontal(fold.location)

    def fold_along_vertical(self, location: int):
        self.x = 2 * location - self.x

    def fold_along_horizontal(self, location: int):
        self.y = 2 * location - self.y


def apply_folds(folds: List[Fold]):
    for fold in folds:
        fold_all_points(fold)


def fold_all_points(fold: Fold):
    global points
    
    for point in points:
        point.apply_fold(fold)


def remove_duplicate_points():
    global points

    unique_points = []
    for point in points:
        if is_in_list(point, unique_points):
            continue
        unique_points.append(point)

    points = unique_points
    

def is_in_list(point: Point, point_list: List[Point]) -> bool:
    for existing_point in point_list:
        if are_equal(point, existing_point):
            return True
    return False


def are_equal(point1: Point, point2: Point) -> bool:
    return point1.x == point2.x and point1.y == point2.y


def print_pattern():
    global points
    x_max = get_x_max()
    y_max = get_y_max()

    for y in range(y_max):
        for x in range(x_max):
            if is_in_list(Point(x,y), points):
                print("X", end="")
            else:
                print(".", end="")
        print("")


def get_x_max() -> int:
    x_coords = [point.x for point in points]
    return max(x_coords) + 1


def get_y_max() -> int:
    y_coords = [point.y for point in points]
    return max(y_coords) + 1


def main():
    global points
    points, folds = parse_input()
    
    # Part 1
    print("=== Part 1 ===")
    fold_all_points(folds[0])
    remove_duplicate_points()
    answer = len(points)
    print("Answer:", answer)

    # Okay to run immediately after Part 1, since repeating a fold does nothing
    # Part 2
    print("=== Part 2 ===")
    apply_folds(folds)
    print_pattern()


def parse_input() -> Tuple[List[Point], List[Fold]]:
    input_file = open("day13_input.txt", "r")
    [input_points, input_folds] = input_file.read().strip().split("\n\n")
    input_file.close()
    
    points = []
    input_points = input_points.split("\n")
    for point in input_points:
        [x, y] = point.strip().split(",")
        points.append(Point(x, y))

    folds = []
    input_folds = input_folds.split("\n")
    for fold in input_folds:
        direction = "vertical" if fold[11] == "x" else "horizontal"
        location = fold[13:].strip()
        folds.append(Fold(direction, location))
        
    return points, folds


if __name__ == "__main__":
    main()
