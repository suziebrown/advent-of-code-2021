from typing import List, Tuple


GRID_WIDTH = 10
GRID_HEIGHT = 10
FLASH_POINT = 10


class Grid:
    def __init__(self, energy: List[List[int]]):
        self.energy = energy
        self.has_flashed = [[False] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.total_flashes = 0          # used in part 1 only
        self.first_sync_time = None     # used in part 2 only

    def simulate_n_steps(self, n: int):
        for _ in range(n):
            self.simulate_one_step()

    def simulate_until_all_flash(self):
        # turns out the answer is <1000, so I didn't change this to a while loop
        for iteration in range(1, 1000):
            self.simulate_one_step()
            flashes_this_step = sum([row.count(True) for row in self.has_flashed])
            if flashes_this_step == GRID_WIDTH * GRID_HEIGHT:
                self.first_sync_time = iteration
                return            

    def simulate_one_step(self):
        self.has_flashed = [[False] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.increment_all_energies()
        self.apply_flashes()
        self.reset_energies()
        flashes_this_step = sum([row.count(True) for row in self.has_flashed])
        self.total_flashes += flashes_this_step
    
    def increment_all_energies(self):
        # x = column index, y = row index, hence the surprising [y][x] indexing everywhere
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                self.energy[y][x] += 1

    def apply_flashes(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.should_flash(x, y):
                    self.flash(x, y)

    def reset_energies(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.has_flashed[y][x]:
                    self.energy[y][x] = 0

    def flash(self, x: int, y: int):
        self.has_flashed[y][x] = True
        self.increment_neighbours(x, y)
        self.flash_neighbours(x, y)

    def increment_neighbours(self, x_here: int, y_here: int):
        neighbours = get_neighbours(x_here, y_here)
        for (x, y) in neighbours:
            self.energy[y][x] += 1

    def flash_neighbours(self, x_here: int, y_here: int):
        neighbours = get_neighbours(x_here, y_here)
        for (x, y) in neighbours:
            if self.should_flash(x, y):
                self.flash(x, y)

    def should_flash(self, x: int, y: int):
        return self.energy[y][x] >= FLASH_POINT and not self.has_flashed[y][x]
    

def get_neighbours(x: int, y: int) -> List[Tuple[int, int]]:
    neighbours = [] 
    if x > 0:
        neighbours.append((x - 1, y))
        if y > 0:
            neighbours.append((x - 1, y - 1))
        if y < GRID_HEIGHT - 1:
            neighbours.append((x - 1, y + 1))
    if x < GRID_WIDTH - 1:
        neighbours.append((x + 1, y))
        if y > 0:
            neighbours.append((x + 1, y - 1))
        if y < GRID_HEIGHT - 1:
            neighbours.append((x + 1, y + 1))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < GRID_HEIGHT - 1:
        neighbours.append((x, y + 1))   
    return neighbours
    

def main():
    energy = parse_input()
    
    # Part 1
    print("=== Part 1 ===")
    grid = Grid(energy)
    grid.simulate_n_steps(100)
    answer = grid.total_flashes
    print("Answer:", answer)

    # Part 2
    # If run straight after part 1, the answer will be 100 too low!
    print("=== Part 2 ===")
    grid = Grid(energy)
    grid.simulate_until_all_flash()
    answer = grid.first_sync_time
    print("Answer:", answer)


def parse_input() -> List[List[int]]:
    input_file = open("day11_input.txt", "r")
    input_lines = input_file.read().strip().split("\n")
    input_file.close()

    energy = [[int(value) for value in list(line)] for line in input_lines]
    return energy


if __name__ == "__main__":
    main()
