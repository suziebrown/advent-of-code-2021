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


from typing import List, Optional


GRID_WIDTH = 100
GRID_HEIGHT = 100


class Point:
    def __init__(self, x, y, risk):
        # y=row index, x=column index, hence the surprising [y][x] indexing
        # NB: x increases Right, y increases Down
        self.x = x
        self.y = y
        self.layer = x + y
        self.risk = risk
        self.risk_distance = None

    def calculate_risk_distance(self, point_left, point_up):
        # May want to calculate the neighbours rather than have them as parameters.
        # In that case, write a wrapper get_risk_distance(self) that gets the neighbours
        # then calls this method with them.
        if point_left is None and point_up is None:
            raise Exception("Expected Left-neighbour and/or Up-neighbour, but got neither")
        if point_left is not None and point_up is not None:
            self.risk_distance = self.risk + min(point_left.risk_distance, point_up.risk_distance)
        elif point_left is None:
            self.risk_distance = self.risk + point_up.risk_distance
        elif point_up is None:
            self.risk_distance = self.risk + point_left.risk_distance


def get_layer(layer_number: int) -> List[Point]:
    global points
    
    x_range = list(range(0, layer_number + 1))
    y_range = [layer_number - x for x in x_range]
    layer = [points[x_range[i]][y_range[i]] for i in range(layer_number + 1)]
    return layer

            
def main():
    global points
    points = parse_input()

    # Test
    
    # Part 1
    print("=== Part 1 ===")
    answer = "?"
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = "?"
    print("Answer:", answer)


def parse_input() -> List[str]:
    input_file = open("day15_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            grid[row][column] = Point(column, row, input_lines[row][column])
        
    return grid


if __name__ == "__main__":
    main()
