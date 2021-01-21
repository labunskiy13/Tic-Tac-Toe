import os
import sys
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
        for row in self.cells:
            if " " in row:
                return False
        return True
        
    def reset(self):
        """Reset board cells. """

        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


class Game:
    """Main game tic-tac class. """

    def __init__(self, board, *args, **kwargs):
        """Initial game instance. """

        self.board = board

    def print_header(self):
        print('Welcom to Tic-Tac-Toe\n')

    def refresh_screen(self):
        os.system('clear')
        self.print_header()
        self.board.display()

    def run(self):
        while True:
            self.refresh_screen()
            self.step('X')
            self.refresh_screen()
            if self.board.is_winner('X'):
                print('\nX wins!\n')
                self.finish()

            if self.board.is_tie():
                print('\nTie game!\n')
                self.finish()

            self.step('O')
            if self.board.is_winner('O'):
                print('\nO wins!\n')
                self.finish()

            if self.board.is_tie():
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
            if self.board.update_cell(selected_row, selected_column, player):
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