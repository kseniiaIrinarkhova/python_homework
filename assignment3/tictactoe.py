# Task 6: More on Classes

class TictactoeException(Exception):
    def __init__(self,message):
        self.message = message 
        super().__init__(self.message)

class Board:
    _valid_moves = {"upper left":[0,0], 
                    "upper center":[0,1], 
                    "upper right":[0,2], 
                    "middle left":[1,0], 
                    "center":[1,1], 
                    "middle right":[1,2], 
                    "lower left":[2,0], 
                    "lower center":[2,1], 
                    "lower right":[2,2]}
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

    def change_turn(self):
        self.turn = 'X' if self.turn == 'O' else 'O'

    def move(self, move_string):
        if move_string in Board._valid_moves:
            move_spot = Board._valid_moves[move_string]
            if self.board_array[move_spot[0]][move_spot[1]] == ' ':
                self.board_array[move_spot[0]][move_spot[1]] = self.turn
                self.change_turn()
            else:
                raise TictactoeException("That spot is taken.")
        else:
            raise TictactoeException("That's not a valid move.")


#check the results
board = Board()
print(board)
print(Board._valid_moves)
board.move('upper left')
# board.move('left')
print(board)