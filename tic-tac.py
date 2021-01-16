import os
os.system("clear")


class Board():
    def __init__(self):
        self.cells = [[" ", " ", " "],
                      [" ", " ", " "], 
		              [" ", " ", " "]]
                      
    def display(self):
        print((" %s | %s | %s " %(self.cells[0][0], self.cells[0][1], self.cells[0][2])))
        print("-----------")
        print((" %s | %s | %s " %(self.cells[1][0], self.cells[1][1], self.cells[1][2])))
        print("-----------")
        print((" %s | %s | %s " %(self.cells[2][0], self.cells[2][1], self.cells[2][2])))

    def update_cell(self, row, column, player):
        if self.cells[row][column] == " ":
            self.cells[row][column] = player

    def is_winner(self, player):
        x_or_y = ''.join(player+player+player)
        if ''.join(self.cells[0]) == x_or_y \
            or ''.join(self.cells[1]) == x_or_y\
            or ''.join(self.cells[2]) == x_or_y\
            or (self.cells[0][0] == self.cells[1][1] == self.cells[2][2] == player)\
            or (self.cells[0][2] == self.cells[1][1] == self.cells[2][0] == player):
            result = True
            if result:
                return True
        return False        

    def is_tie(self):
        for row in self.cells:
            if row.count(" ") != 0:
                return False
        return True          
                    
        
    def reset(self):
        self.cells = [[" ", " ", " "],
                      [" ", " ", " "], 
		              [" ", " ", " "]] 


board = Board()


def print_header():
    print("Welcom to Tic-Tac-Toe\n")


def refresh_screen():
    os.system("clear")
    print_header()
    board.display()


while True:
    refresh_screen()
    x_row = (int(eval(input("\nX) Plase choose row >"))-1))
    x_column = (int(eval(input("\nX) Plase choose column >"))-1))
    board.update_cell(x_row, x_column, "X")
    refresh_screen()
    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break    

    o_row = (int(eval(input("\nO) Plase choose row >"))-1))
    o_column = (int(eval(input("\nO) Plase choose column >"))-1))
    board.update_cell(o_row, o_column, "O")
    if board.is_winner("O"):
        print("\nO wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break      