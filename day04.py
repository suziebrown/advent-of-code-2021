NUMBER_OF_BOARDS = 100
ROWS_PER_BOARD = 5
COLUMNS_PER_BOARD = 5

def parse_input() -> list[str]:
    
    input_file = open("day04_input.txt", "r")
    raw_input = input_file.read().split("\n\n")

    numbers_drawn = raw_input[0].split(",")

    boards_rows = [split_rows(raw_board) for raw_board in raw_input[1:NUMBER_OF_BOARDS + 1]]
    boards = [split_columns(board_rows) for board_rows in boards_rows]
        
    input_file.close()
    return (numbers_drawn, boards)


def split_rows(raw_board: str) -> list[str]:
    board_rows = raw_board.strip().split("\n")
    return board_rows


def split_columns(board_rows: list[str]) -> list[list[str]]:
    board = [row.split() for row in board_rows]
    return board


def get_winner_score(numbers_drawn: list[str], boards: list[list[list[str]]]):
    for number in numbers_drawn:
        mark_boards(number, boards)
        
        winner_index = get_winner_or_none(boards)
        if winner_index is not None:
            winning_board = boards[winner_index]
            score = get_score(winning_board, number)
            return score

    raise Exception("All numbers were drawn but no winner was found")


def get_loser_score(numbers_drawn: list[str], boards: list[list[list[str]]]):
    boards_bingo_status = [0] * NUMBER_OF_BOARDS
    loser_index = None
    
    for number in numbers_drawn:
        mark_boards(number, boards)
        update_boards_bingo_status(boards, boards_bingo_status)
        
        print(boards_bingo_status)

        if loser_index is None:
            loser_index = get_loser_or_none(boards_bingo_status)
            
        if is_game_over(boards_bingo_status):
            losing_board = boards[loser_index]

            print("Losing board:", losing_board)
            print("Number just drawn:", number)
            
            score = get_score(losing_board, number)
            return score

    raise Exception("All numbers were drawn but no loser was found")


def mark_boards(number: str, boards: list[list[list[str]]]):
    for board in boards:
        for row in range(ROWS_PER_BOARD):
            for column in range(COLUMNS_PER_BOARD):
                if board[row][column] == number:
                    board[row][column] = None


def update_boards_bingo_status(boards: list[list[list[str]]], boards_bingo_status: list[int]):
    for board_index in range(NUMBER_OF_BOARDS):
        if boards_bingo_status[board_index] == 0 and has_bingo(boards[board_index]):
            boards_bingo_status[board_index] = 1


def get_winner_or_none(boards: list[list[list[str]]]) -> int:
    for board_index, board in enumerate(boards):
        if has_bingo(board):
            return board_index
        
    return None


def get_loser_or_none(boards_bingo_status: list[int]) -> int:
    number_of_bingos = sum(boards_bingo_status)
    
    if number_of_bingos == NUMBER_OF_BOARDS - 1:
        loser_index = boards_bingo_status.index(0)
        return loser_index
        
    return None


def has_bingo(board: list[list[str]]) -> bool:
    for row in board:
        if count_marked(row) == COLUMNS_PER_BOARD:
            return True
            
    for column in transpose(board):
        if count_marked(column) == ROWS_PER_BOARD:
            return True

    return False


def is_game_over(boards_bingo_status: list[int]) -> bool:
    number_of_bingos = sum(boards_bingo_status)
    return number_of_bingos == NUMBER_OF_BOARDS


def get_score(winning_board: list[list[str]], last_number_drawn: str) -> int:
    winning_board_int = [[int(number) for number in row if number is not None] for row in winning_board]
    row_sums = [sum(row) for row in winning_board_int]
    score = sum(row_sums) * int(last_number_drawn)
    return score


def count_marked(row_or_column: list[str]) -> int:
    return sum(x is None for x in row_or_column)


def transpose(board: list[list[str]]) -> list[list[str]]:
    transposed_board = [[row[column_index] for row in board] for column_index in range(COLUMNS_PER_BOARD)]
    return transposed_board


def main():
    (numbers_drawn, boards) = parse_input()

    ## Part 1
    print("=== Part 1 ===")
    score = get_winner_score(numbers_drawn, boards)
    print("Answer:", score)
    
    ## Part 2
    print("=== Part 2 ===")
    score = get_loser_score(numbers_drawn, boards)
    print("Answer:", score)
    

if __name__ == "__main__":
    main()
