from Grid import Grid, print_case_list
from solve import solve


def main():
    str_grid = '_1_8___27#______9__#___7____3#83__1____#_614_759_#9____61_2#5___29_7_#__8_7____#627_____9'
    grid = Grid()
    grid.string_to_grid(str_grid)

    solve(grid)
    grid.txt_print()




if __name__ == '__main__':
    main()