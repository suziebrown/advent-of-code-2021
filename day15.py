# STRATEGY
# * Make the (not necessarily true) assumption that the only useful moves are Down and Right
#   (i.e. doubling back never reduces risk)
# * The Down/Right restriction means each point in the grid has a well-defined distance from the start
#   (Manhattan distance), and the distance start->end is width+height=198
# * Even so, the number of possible paths is 198C99~=2e58, too big for exhaustive search
# * But we can consider the "layer" at each distance (1 to 198) from start, and calculate the
#   "risk distance" (=total risk of best path from start) of each point in each layer, iteratively.
# * e.g. at distance 1 there are two possible points, Down or Right, and the risk distance of each
#   from start is the risk level at that point.
# * In layer n, there are (n+1) points, and (2n) possible path segments from the previous layer
# * Calculating the lowest-risk path to a given point P in layer n, from any point in layer (n-1)
#   just requires checking 2 path segments (from Q and Q', the points Left of or Above P) and setting
#   risk(P) = min{risk(start->Q)+risk(Q), risk(start->Q')+risk(Q')}.
#   Points along an edge are even easier!
# * We have to repeat this calculation (n+1) times in each layer up to distance 99, then the number
#   of points per layer starts to decrease again, for a total of 100+98*99 = 9,802 calculations.
#   This seems doable!

from typing import List, Tuple, Optional

# These values should be 100 for Part 1, or 500 for Part 2 (I know, I shouldn't really hard-code them)
GRID_WIDTH = 500
GRID_HEIGHT = 500
NUMBER_OF_LAYERS = GRID_HEIGHT + GRID_WIDTH - 2


class Point:
    def __init__(self, x, y, risk):
        # y=row index, x=column index, hence the surprising [y][x] indexing
        # NB: x increases Right, y increases Down
        self.x = x
        self.y = y
        self.layer = x + y
        self.risk = int(risk)
        self.risk_distance = None

    def get_risk_distance(self):
        if self.x == 0 and self.y == 0:
            self.risk_distance = 0
        else:
            (left_neighbour, up_neighbour) = self.get_left_and_up_neighbours()
            self.risk_distance = self.calculate_risk_distance(left_neighbour, up_neighbour)

    def get_left_and_up_neighbours(self):  # -> Tuple[Optional[Point], Optional[Point]]
        if self.x == 0:
            left_neighbour = None
        else:
            left_neighbour_x = self.x - 1
            left_neighbour_y = self.y
            left_neighbour = points[left_neighbour_y][left_neighbour_x]
        if self.y == 0:
            up_neighbour = None
        else:
            up_neighbour_x = self.x
            up_neighbour_y = self.y - 1
            up_neighbour = points[up_neighbour_y][up_neighbour_x]
        return left_neighbour, up_neighbour

    def calculate_risk_distance(self, left_neighbour, up_neighbour) -> int:
        if left_neighbour is None and up_neighbour is None:
            raise Exception("Expected Left-neighbour and/or Up-neighbour, but got neither")
        if left_neighbour is not None and up_neighbour is not None:
            risk_distance = self.risk + min(left_neighbour.risk_distance, up_neighbour.risk_distance)
        elif left_neighbour is None:
            risk_distance = self.risk + up_neighbour.risk_distance
        elif up_neighbour is None:
            risk_distance = self.risk + left_neighbour.risk_distance
        return risk_distance


def calculate_risk_distances():
    for layer_number in range(0, NUMBER_OF_LAYERS + 1):
        points_in_layer = get_layer(layer_number)
        for point in points_in_layer:
            point.get_risk_distance()


def get_layer(layer_number: int) -> List[Point]:
    global points

    if layer_number <= GRID_WIDTH - 1:
        x_range = list(range(0, layer_number + 1))
        y_range = [layer_number - x for x in x_range]
    else:
        x_range = list(range(layer_number - GRID_WIDTH + 1, GRID_WIDTH))
        y_range = [layer_number - x for x in x_range]

    layer = [points[y_range[i]][x_range[i]] for i in range(len(x_range))]
    return layer

            
def main():
    global points
    points = parse_input()

    # To switch between Part 1/2, change the input filename and the WIDTH/HEIGHT constants.
    calculate_risk_distances()
    answer = points[GRID_HEIGHT - 1][GRID_WIDTH - 1].risk_distance
    print("Answer:", answer)


def parse_input() -> List[List[Point]]:
    input_file = open("day15_part2_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            grid[row][column] = Point(column, row, input_lines[row][column])
        
    return grid


if __name__ == "__main__":
    main()
