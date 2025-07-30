# Task 6: More on Classes

class TictactoeException(Exception):
    def __init__(self):
        self.message = "Tic Tac Toe Exception!"
        super().__init__(self.message)

class Board:
    _valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = 'X'

    def __str__(self):
        result = ""
        count = 0
        for row in self.board_array:
            line = '|'.join(f' {cell} ' for cell in row) #row line
            result += line + '\n'
            if count<2:
                result += '-'*(len(row)*4 - 1) + '\n' # separator line
                count +=1
        return result    

board = Board()
print(str(board))
print(Board._valid_moves)