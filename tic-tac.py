import os
import sys
from random import randint
os.system('clear')


class Board:

    def __init__(self, *args, **kwargs):
        """Initial board instance. """

        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display(self):
        print((' %s | %s | %s ' %(self.cells[0][0], self.cells[0][1], self.cells[0][2])))
        print('-----------')
        print((' %s | %s | %s ' %(self.cells[1][0], self.cells[1][1], self.cells[1][2])))
        print('-----------')
        print((' %s | %s | %s ' %(self.cells[2][0], self.cells[2][1], self.cells[2][2])))

    def update_cell(self, row, column, player):
        if self.cells[row][column] == " ":
            self.cells[row][column] = player
             
    def place_check(self, row, column):
        if self.cells[row][column] == " ":
            return True
        else:
            print("this cell is occupied, repeat the move and be careful!)")
            return False

    def is_winner(self, player, pole):
        winner = player*3  # 'XXX' or 'OOO'

        # Проверяем строки
        for cell in pole:
            if ''.join(cell) == winner:
                return True

        # Мы развернули нашу матрицу на 90 градусов, и тпперь проверяем столбцы.
        for cell in list(zip(*pole)):
            if ''.join(cell) == winner:
                return True

        # Смотрим первую диагональ
        if pole[0][0] + pole[1][1] + pole[2][2] == winner:
            return True

        # Смотрим вторую диагональ
        if pole[0][2] + pole[1][1] + pole[2][0] == winner:
            return True

        return False

    def is_tie(self, pole):
        # TODO: Fix this loops!

        for row in pole:
            if " " in row:
                return False
        return True
        
    def reset(self):
        """Reset board cells. """

        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


class AiPlayer:

    def init(self, board, *args, **kwargs):
        self.cells = board.cells
        self.board = board

    def minimax(self, board, depth, is_ai_turn):
        scores = {
                  "X": -100,
                  "O": 100,
                  'tie': 0
                 }
        field = [self.cells[y].copy() for y in range(3)]
        if Board.is_winner(self, "O", field):
            return scores["O"]
        if Board.is_winner(self, "X", field):
            return scores["X"]
        if Board.is_tie(self, field):
            return scores['tie']

        if is_ai_turn:
            # выбираем ход который нам выгодней
            best_score = - sys.maxsize
            for y in range(3):
                for x in range(3):
                    if board[y][x] == " ":
                        field[y][x] = "O"
                        score = AiPlayer.minimax(self, field, depth + 1, False)
                        field[y][x] = " "
                        best_score = max(best_score, score)
        else:
            # противник выбирает ход который нам не выгоден
            best_score = sys.maxsize
            for y in range(3):
                for x in range(3):
                    if field[y][x] == " ":
                        field[y][x] = "X"
                        score = AiPlayer.minimax(self, board, depth + 1, True)
                        field[y][x] = " "
                        best_score = min(best_score, score)
        return best_score             

    def step_ai(self):
        move = None
        field = [self.cells[y].copy() for y in range(3)]
        best_score = -sys.maxsize
        for y in range(3):
            for x in range(3):
                if field[y][x] == " ":
                    field[y][x] = "O"
                    score = AiPlayer.minimax(self, field, 0, False)
                    field[y][x] = " "
                    if score > best_score:
                        best_score = score
                        move = (x, y)
        return move


class Game:
    """Main game tic-tac class. """

    def __init__(self, board, *args, **kwargs):
        """Initial game instance. """
        self.cells = board.cells
        self.board = board

    def print_header(self):
        print('Welcom to Tic-Tac-Toe\n')

    def refresh_screen(self):
        os.system('clear')
        self.print_header()
        self.board.display()

    def run(self):
        single_or_company = input("single or company? (S/C) :")
        while True:
            self.refresh_screen()
            self.step('X')
            self.refresh_screen()
            if self.board.is_winner('X',self.cells):
                print('\nX wins!\n')
                self.finish()

            if self.board.is_tie(self.cells):
                print('\nTie game!\n')
                self.finish()

            if single_or_company == "S":
                AiPlayer.step_ai(self)
            else:    
                self.step('O')

            if self.board.is_winner('O',self.cells):
                print('\nO wins!\n')
                self.finish()

            if self.board.is_tie(self.cells):
                print('\nTie game!\n')
                self.finish()

    def step(self, player):
        while True:
            """One game step. Select row, column and update cell. """
            selected_row = int(
                input('\n{0}) Please choose row >'.format(player))
            )-1
            print('selected_row: ', selected_row, type(selected_row))
            selected_column = int(
                input('\n{0}) Please choose column >'.format(player))
            )-1
            if self.board.place_check(selected_row, selected_column):
                self.board.update_cell(selected_row, selected_column, player)
                break

    def finish(self):
        play_again = input('Would you like to play again? (Y/N) > ').upper()
        if play_again == 'Y':
            self.board.reset()
        else:
            sys.exit()


if __name__ == "__main__":
    # Your code start here

    board = Board()
    game = Game(board)
    game.run()