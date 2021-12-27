file = open("day4_input.txt", "r")

total_file_length = 0

with open("day4_input.txt", 'r') as fp: total_file_length = len(fp.readlines())

class Bingo:

    drawn_numbers = file.readline().rstrip()
    drawn_numbers = drawn_numbers.split(',')
    lines = file.readlines()

    board_numbers = 0
    line_index = 1
    max_length = total_file_length

    boards = []
    checked_boards = []
    winner_boards = []

    def __init__(self):

        while self.line_index < self.max_length:
            
            board = []
            checked_board = []

            for line in self.lines[self.line_index:self.line_index + 5]:
                board.append(line.split())
                checked_board.append([False,False,False,False, False])
            
            self.boards.append(board)
            self.checked_boards.append(checked_board)
            self.board_numbers += 1
            self.line_index = self.line_index + 6
   
    def draw_balls(self):
        for drawn_number in self.drawn_numbers:
            for board in range(self.board_numbers):
                for i in range(5):
                    for j in range(5):
                        
                        if self.boards[board][i][j] == drawn_number: self.checked_boards[board][i][j] = True    
                        # Board Wins
                        if board not in self.winner_boards and self.check_if_board_wins(board) == True:
                            self.winner_boards.append(board)
                            print(f'Board {board} wins with points: {self.calcuate_winner_points(board, drawn_number)}')

    def check_if_board_wins(self, board_index):
       
        #check rows
        for i in range(5):
            if self.checked_boards[board_index][i] == [True, True, True, True, True]:
                return True

        for i in range(5):
            column_matches = True
            for j in range(5):
                if self.checked_boards[board_index][j][i] == False:
                    column_matches = False
            if column_matches: return True  

        return False

    def calcuate_winner_points(self, board_index, drawn_number):
        total_points = 0

        for i in range(5):
            for j in range(5):
                if self.checked_boards[board_index][i][j] == False:
                    total_points += int(self.boards[board_index][i][j])

        return total_points * int(drawn_number)

bingo = Bingo()

print('Silver and Gold Star Solutions (First Winner and Last Winner):')
bingo.draw_balls()
