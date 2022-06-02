from grid_print_function import *
from winner_check import *
player_symbol = "X"
step = 1
grid_list = [["_" for cell in range(3)] for raw in range(3)]


def user_input():
    while True:
        try:
            x, y = map(int, input("> ").split())
            check = grid_list[x - 1][y - 1]
        except IndexError:
            print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")
        else:
            if x == 0 or y == 0:
                print("Coordinates should be from 1 to 3!")
            elif grid_list[int(x)-1][int(y)-1] == "_":
                grid_list[int(x)-1][int(y)-1] = player_symbol
                break
            else:
                print("This cell is occupied! Choose another one!")


def change_symbol():
    global player_symbol
    if player_symbol == "X":
        player_symbol = "O"
    else:
        player_symbol = "X"


print_gird(grid_list)
while step < 5:
    user_input()
    print_gird(grid_list)
    step += 1
    change_symbol()
while step < 10:
    user_input()
    print_gird(grid_list)
    if winner(grid_list, player_symbol):
        break
    step += 1
else:
    print("Draw")


