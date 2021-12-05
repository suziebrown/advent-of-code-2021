class Point:
    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return self.x + "," + self.y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_all_points(self) -> list[Point]:
        if self.is_horizontal():
            return self.get_all_points_horizontal()
        if self.is_vertical():
            return self.get_all_points_vertical()
        return self.get_all_points_diagonal()

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def get_all_points_horizontal(self) -> list[Point]:
        points = list[Point]()
        for x in range(self.x_min(), self.x_max() + 1):
            points.append(Point(x = str(x), y = self.start.y))
        return points

    def get_all_points_vertical(self) -> list[Point]:
        points = list[Point]()
        for y in range(self.y_min(), self.y_max() + 1):
            points.append(Point(x = self.start.x, y = str(y)))
        return points

    def get_all_points_diagonal(self) -> list[Point]:
        points = list[Point]()
        is_diagonal_up = self.is_diagonal_up()
        y = self.y_min() if is_diagonal_up else self.y_max()
        for x in range(self.x_min(), self.x_max() + 1):
            points.append(Point(x = str(x), y = str(y)))
            y = y + 1 if is_diagonal_up else y - 1
        return points

    def is_diagonal_up(self) -> bool:
        x1 = int(self.start.x)
        x2 = int(self.end.x)
        y1 = int(self.start.y)
        y2 = int(self.end.y)
        is_diagonal_bl_to_tr = x1 <= x2 and y1 <= y2
        is_diagonal_tr_to_bl = x1 >= x2 and y1 >= y2
        return is_diagonal_bl_to_tr or is_diagonal_tr_to_bl

    def x_min(self) -> int:
        x1 = int(self.start.x)
        x2 = int(self.end.x)
        return x1 if x1 <= x2 else x2

    def x_max(self) -> int:
        x1 = int(self.start.x)
        x2 = int(self.end.x)
        return x1 if x1 >= x2 else x2

    def y_min(self) -> int:
        y1 = int(self.start.y)
        y2 = int(self.end.y)
        return y1 if y1 <= y2 else y2

    def y_max(self) -> int:
        y1 = int(self.start.y)
        y2 = int(self.end.y)
        return y1 if y1 >= y2 else y2


def main():
    lines = parse_input()
    
    ## Part 1
    print("=== Part 1 ===")
    hv_lines = [line for line in lines if line.is_horizontal() or line.is_vertical()]
    answer = len(get_points_with_multiple_vents(hv_lines))
    
    print("Answer:", answer)

    ## Part 2
    print("=== Part 2 ===")
    answer = len(get_points_with_multiple_vents(lines))
    print("Answer:", answer)


def parse_input() -> list[Line]:
    input_file = open("day05_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    lines = list[Line]()
    for input_line in input_lines:
        start_end = input_line.split(" -> ")
        start = start_end[0].split(",")
        end = start_end[1].split(",")
        
        start_point = Point(x = start[0], y = start[1])
        end_point = Point(x = end[0], y = end[1])
        line = Line(start = start_point, end = end_point)
        lines.append(line)
        
    return lines


def get_points_with_multiple_vents(lines: list[Line]) -> list[Point]:
    points_with_multiple_vents = list[Point]()
    vent_counts = dict[str, int]()

    for line in lines:
        points_in_line = line.get_all_points()
        update_vent_counts(points_in_line, vent_counts)

    points_with_multiple_vents = [key for key in vent_counts.keys() if vent_counts[key] > 1]
    
    return points_with_multiple_vents


def update_vent_counts(points: list[Point], vent_counts: dict[str, int]):
    for point in points:
        key = point.to_string()
        previous_count = vent_counts[key] if key in vent_counts.keys() else 0
        vent_counts.update({key: previous_count + 1})


if __name__ == "__main__":
    main()


    
