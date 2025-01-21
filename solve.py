from Strategy.HiddenSingle import HiddenSingle
from Strategy.NakedPairs import NakedPairs

STRAT_ORDER = [HiddenSingle, NakedPairs]

def solve(grid):
    while grid.get_nb_case_fill() < 81:
        grid.txt_print()
        print('\n*********************************\n\n')
        if not solve_step(grid):
            break

def solve_step(grid):
    grid.update_possibles()
    for strat in STRAT_ORDER:
        s = strat(grid)
        s.apply()
        if s.effect:
            s.print_name()
            return 1
    print("aucune stratégie n'a eu un effet")
    return 0


if __name__ == '__main__':
        solve()