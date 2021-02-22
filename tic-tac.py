import os
import sys
from random import randint
import csv
import datetime
import time
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

    def is_winner(self, player):
        winner = player*3  # 'XXX' or 'OOO'

        # Проверяем строки
        for cell in self.cells:
            if ''.join(cell) == winner:
                return True

        # Мы развернули нашу матрицу на 90 градусов, и тпперь проверяем столбцы.
        for cell in list(zip(*self.cells)):
            if ''.join(cell) == winner:
                return True

        # Смотрим первую диагональ
        if self.cells[0][0] + self.cells[1][1] + self.cells[2][2] == winner:
            return True

        # Смотрим вторую диагональ
        if self.cells[0][2] + self.cells[1][1] + self.cells[2][0] == winner:
            return True

        return False

    def is_tie(self):
        # TODO: Fix this loops!

        for row in self.cells:
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
        self.save_game = game.save_game

    def step_ai(self):
        selected_row, selected_column = randint(0, 2), randint(0, 2)
        while self.cells[selected_row][selected_column] != " ":
            selected_row, selected_column = randint(0, 2), randint(0, 2)
        self.save_game(["O", selected_row, selected_column])
        return self.board.update_cell(selected_row, selected_column, "O")


class Game:
    """Main game tic-tac class. """

    def __init__(self, board, *args, **kwargs):
        """Initial game instance. """
        self.cells = board.cells
        self.board = board
    
    def save_game(self, act):
        FILENAME = "game.csv"
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file, delimiter=":")
            writer.writerow(act)

    def print_header(self):
        print('Welcom to Tic-Tac-Toe\n')

    def refresh_screen(self):
        os.system('clear')
        self.print_header()
        self.board.display()

    def run(self):
        date = datetime.datetime.today().strftime("%d.%m.%Y")
        when = datetime.datetime.today().strftime("%H:%M:%S")
        self.print_header()
        time.sleep(1)
        single_or_company = input("single or company? (S/C) :")
        self.save_game(["game number", date, when])
        while True:
            self.refresh_screen()
            self.step('X')
            self.refresh_screen()
            if self.board.is_winner('X'):
                self.refresh_screen()
                print('\nX wins!\n')
                self.save_game(["X wins!"])
                self.finish()

            if self.board.is_tie():
                self.refresh_screen()
                print('\nTie game!\n')
                self.save_game(["Tie game!"])
                self.finish()

            if single_or_company == "S":
                AiPlayer.step_ai(self)
            else:    
                self.step('O')

            if self.board.is_winner('O'):
                self.refresh_screen()
                print('\nO wins!\n')
                self.save_game(["O wins!"])
                self.finish()

            if self.board.is_tie():
                self.refresh_screen()
                print('\nTie game!\n')
                self.save_game(["Tie game!"])
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
                self.save_game([player, selected_row, selected_column])
                break

    def finish(self):
        play_again = input('Would you like to play again? (Y/N) > ').upper()
        if play_again == 'Y':
            self.save_game(["new game"])
            self.board.reset()
            self.run()
        else:
            sys.exit()


if __name__ == "__main__":
    # Your code start here

    board = Board()
    game = Game(board)
    game.run()