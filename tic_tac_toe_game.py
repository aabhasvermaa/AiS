import math

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the Tic-Tac-Toe board
class TicTacToe:
    def __init__(self):
        self.board = [EMPTY] * 9
        self.current_player = PLAYER_X

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i + 1], '|', self.board[i + 2])
            if i < 6:
                print("---------")

    def make_move(self, position):
        if self.board[position] == EMPTY:
            self.board[position] = self.current_player
            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
            return True
        else:
            return False

    def is_game_over(self):
        return self.check_winner() or not any([cell == EMPTY for cell in self.board])

    def check_winner(self):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != EMPTY:
                return self.board[combo[0]]
        return None

    def available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == EMPTY]

# Min-Max algorithm with Alpha-Beta Pruning
def min_max_alpha_beta(board, depth, alpha, beta, is_maximizing):
    if board.is_game_over() or depth == 0:
        winner = board.check_winner()
        if winner == PLAYER_X:
            return -1
        elif winner == PLAYER_O:
            return 1
        else:
            return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in board.available_moves():
            board.make_move(move)
            eval = min_max_alpha_beta(board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            board.board[move] = EMPTY
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.available_moves():
            board.make_move(move)
            eval = min_max_alpha_beta(board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            board.board[move] = EMPTY
            if beta <= alpha:
                break
        return min_eval

# Find the best move using Min-Max with Alpha-Beta Pruning
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for move in board.available_moves():
        board.make_move(move)
        eval = min_max_alpha_beta(board, 9, -math.inf, math.inf, False)
        board.board[move] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Main game loop
if __name__ == "__main__":
    game = TicTacToe()
    
    while not game.is_game_over():
        game.print_board()
        
        if game.current_player == PLAYER_X:
            position = int(input("Enter your move (0-8): "))
            if position < 0 or position > 8 or not game.make_move(position):
                print("Invalid move. Try again.")
            else:
                game.make_move(position)
        else:
            print("AI is thinking...")
            best_move = find_best_move(game)
            game.make_move(best_move)

    game.print_board()
    winner = game.check_winner()
    if winner:
        print(f"The winner is {winner}")
    else:
        print("It's a draw!")
