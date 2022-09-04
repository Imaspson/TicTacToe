class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        #we can use a simple list to represent a 3x3 board.
        self.current_winner = None
        #keep track of the winner

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3 for i in range(3)]]:
            print('| ' + ' | ',join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 | etc tells us that number corresponds to what box
        number_board = [[str(i) for i in range(j + 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | ',join(row) + ' |')