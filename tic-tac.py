import os
os.system("clear")


class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print((" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3])))
        print("-----------")
        print((" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6])))
        print("-----------")
        print((" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9])))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        for combo in [[1, 2, 3], [1, 4, 7],[4 , 5, 6], [2, 5, 8], [3, 6, 9], [7, 8, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result == True:
                return True
        return False        

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False    

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] 


board = Board()


def print_header():
    print("Welcom to Tic-Tac-Toe\n")


def refresh_screen():
    os.system("clear")
    print_header()
    board.display()


while True:
    refresh_screen()
    x_choice = int(eval(input("\nX) Plase choose 1 - 9. >")))
    board.update_cell(x_choice, "X")
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

    o_choice = int(eval(input("\nO) Plase choose 1 - 9. >")))
    board.update_cell(o_choice, "O")
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
