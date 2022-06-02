def print_gird(grid_list):
    border = "---------"
    print(border)
    for i in range(len(grid_list)):
        print("|", grid_list[i][0], grid_list[i][1], grid_list[i][2], "|")
    print(border)
