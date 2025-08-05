# Task 6: More on Classes

#custom exception class for Tic Tac Toe game
class TictactoeException(Exception):
    def __init__(self,message):
        self.message = message 
        super().__init__(self.message)

#Class for Tic Tac Toe board
class Board:
    #static property, collect dictionary of moves and their location on board
    _valid_moves = {"upper left":[0,0], 
                    "upper center":[0,1], 
                    "upper right":[0,2], 
                    "middle left":[1,0], 
                    "center":[1,1], 
                    "middle right":[1,2], 
                    "lower left":[2,0], 
                    "lower center":[2,1], 
                    "lower right":[2,2]}
    #constructor for board
    def __init__(self):
        #declare clear board
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        #initialize first turn
        self.turn = 'X'
        #initialize available spots - all board is empty - 9 spots
        self.free_spots = 9

    #method to get the string representation of current board state
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

    #method for changing turn
    def change_turn(self):
        self.turn = 'X' if self.turn == 'O' else 'O'

    #method for move
    def move(self, move_string):
        #check for valid move
        if move_string in Board._valid_moves:
            #get move coordinates
            move_spot = Board._valid_moves[move_string]
            #check for empty spot
            if self.board_array[move_spot[0]][move_spot[1]] == ' ':
                #make a move
                self.board_array[move_spot[0]][move_spot[1]] = self.turn
                #decreace amount of available spots
                self.free_spots -=1
                #change the turn
                self.change_turn()
            else:
                raise TictactoeException("That spot is taken.")
        else:
            raise TictactoeException("That's not a valid move.")
    
    #method that check if player won
    #player:string - 'X or 'O'
    def check_winner(self, player):
        #check all possible win combinations
        return ( 
            self.board_array[0][0] == self.board_array[0][1] == self.board_array[0][2] == player or
            self.board_array[1][0] == self.board_array[1][1] == self.board_array[1][2] == player or
            self.board_array[2][0] == self.board_array[2][1] == self.board_array[2][2] == player or
            self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] == player or
            self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] == player or
            self.board_array[0][0] == self.board_array[1][0] == self.board_array[2][0] == player or
            self.board_array[0][1] == self.board_array[1][1] == self.board_array[2][1] == player or
            self.board_array[0][2] == self.board_array[1][2] == self.board_array[2][2] == player 
        )

    #method that analyze the board
    def whats_next(self):
        #check first player
        if self.check_winner('X') :
            return (True, "X has won")
        #check second player
        if self.check_winner('O'):
            return (True, "O has won")
        #if there is no free spots and no winners - finish the game
        if self.free_spots == 0 :
            return (True, "Cat's Game")
        #continue playing
        return (False, self.get_turn())
    
    #method that return current turn
    def get_turn(self):
        return "X's turn" if self.turn == 'X' else "O's turn"
        


#check the results
board = Board()
print(board)
game_finished = False
result = ''
while not game_finished:
    move = input(f'{board.get_turn()}: ')
    try:
        board.move(move)
    except TictactoeException as e:
        print(e)
    else:
        print(board)
        game_finished, result = board.whats_next()

print(result)
