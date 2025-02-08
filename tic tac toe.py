class TicTacToe:
    def __init__(self, boardsize=3):
        self.boardsize = boardsize
        self.board = [[' ' for _ in range(self.boardsize)] for _ in range(self.boardsize)]
        self.current_player = 'X'
    
    def print_board(self):
        print("  " + "   ".join(map(str, range(self.boardsize))))
        print("  " + "----" * self.boardsize)
        for i, row in enumerate(self.board):
            print(i, " | ".join(row))
            print("  " + "----" * self.boardsize)
    
    def check_winner(self):
        # Check rows and columns
        for i in range(self.boardsize):
            if all(self.board[i][j] == self.current_player for j in range(self.boardsize)):
                return True
            if all(self.board[j][i] == self.current_player for j in range(self.boardsize)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(self.boardsize)):
            return True
        if all(self.board[i][self.boardsize - 1 - i] == self.current_player for i in range(self.boardsize)):
            return True
        
        return False
    
    def make_move(self, row, col):
        if 0 <= row < self.boardsize and 0 <= col < self.boardsize and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return False
        else:
            print("Invalid move. Try again.")
            return None
    
    def play(self):
        moves = 0
        max_moves = self.boardsize * self.boardsize
        while moves < max_moves:
            self.print_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter row and column (e.g., 0 1): ").split())
                if self.make_move(row, col):
                    return
                moves += 1
            except ValueError:
                print("Invalid input. Enter two numbers separated by space.")
        
        self.print_board()
        print("It's a tie!")

# Start the game
game = TicTacToe()
game.play()
