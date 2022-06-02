def winner(grid_list, player_symbol):
    columns_list = [[grid_list[0][i], grid_list[1][i], grid_list[2][i]] for i in range(3)]
    diagonal_1 = [grid_list[0][0], grid_list[1][1], grid_list[2][2]]
    diagonal_2 = [grid_list[2][0], grid_list[1][1], grid_list[0][2]]
    for row in grid_list:
        if all([symbol == player_symbol for symbol in row]):
            print(f"{player_symbol} wins")
            return True
    for column in columns_list:
        if all([symbol == player_symbol for symbol in column]):
            print(f"{player_symbol} wins")
            return True
    if all([symbol == player_symbol for symbol in diagonal_1]):
        print(f"{player_symbol} wins")
        return True
    elif all([symbol == player_symbol for symbol in diagonal_2]):
        print(f"{player_symbol} wins")
        return True
    else:
        return False
