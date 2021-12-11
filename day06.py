from typing import List


RESET_VALUE = 6
INITIAL_VALUE = 8
DISTINCT_VALUES = INITIAL_VALUE + 1


def initial_timer_counts(input_timers: List[str]) -> List[int]:
    timer_counts = [None] * DISTINCT_VALUES
    timers = list(map(int, input_timers))
    
    for value in range(0, DISTINCT_VALUES):
        timer_counts[value] = timers.count(value)

    return timer_counts


def next_day(timer_counts: List[int]) -> List[int]:
    updated_timer_counts = [0] * len(timer_counts)

    for value in range(1, DISTINCT_VALUES):
        updated_timer_counts[value - 1] = timer_counts[value]
        
    updated_timer_counts[RESET_VALUE] += timer_counts[0]
    updated_timer_counts[INITIAL_VALUE] = timer_counts[0]
    
    return updated_timer_counts


def fast_forward(timer_counts: List[int], days: int) -> List[int]:
    for _ in range(days):
        timer_counts = next_day(timer_counts)

    return timer_counts
    

def main():
    timers = parse_input()
    counts = initial_timer_counts(timers)
    
    ## Part 1
    print("=== Part 1 ===")
    counts_day_80 = fast_forward(counts, 80)
    answer = sum(counts_day_80)
    print("Answer:", answer)

    ## Part 2
    print("=== Part 2 ===")
    counts_day_256 = fast_forward(counts, 256)
    answer = sum(counts_day_256)
    print("Answer:", answer)


def parse_input() -> List[str]:
    input_file = open("day06_input.txt", "r")
    input_timers = input_file.read().strip().split(",")
    input_file.close()
    return input_timers


if __name__ == "__main__":
    main()
