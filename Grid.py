from Case import Case


class Grid(object):

    def __init__(self):
        self.cases = [[Case() for _ in range(9)]  for _ in range(9)]

    # remplis une case
    def set_value(self, li, co, val):
        self.cases[li][co].set_value(val)

    # renvoie le nb de cases remplies
    def get_nb_case_fill(self):
        count = 0
        for li in range(9):
            for co in range(9):
                if self.cases[li][co].has_value():
                    count += 1
        return count

    # renvoie une ligne donnée sous forme de liste
    def get_line(self, li):
        return [self.cases[li][co] for co in range(9)]

    # renvoie une colonne donnée sous forme de liste
    def get_col(self, co):
        return [self.cases[li][co] for li in range(9)]

    # renvoie la valeur (si il y en a une) d'une case donnée
    def get_case_value(self, li, co):
        return self.cases[li][co].get_value()

    # renvoie les possibles d'une case donnée
    def get_case_possibles(self, li, co):
        return self.cases[li][co].get_possibles()

    # convertit une grille sous forme textuelle en object python
    def string_to_grid(self, str):
        if len(str) != 89:
            print("Format inadapté")
        else:
            i = 0
            while i < 90:
                if str[i] != '_':
                    self.cases[i // 10][i % 10].set_value(str[i])
                i += 1
                if i % 10 == 9:
                    i += 1


    def txt_print(self):
        for li in range(9):
            grid_str = ''
            for co in range(9):
                if self.cases[li][co].has_value():
                    grid_str += str(self.cases[li][co].get_value())
                else:
                    grid_str += '_'
                grid_str += ' '
                if co % 3 == 2:
                    grid_str += '  '
            print(grid_str)
            if li % 3 == 2:
                print()

if __name__ == '__main__':
    str_grid = '_1_8___27#______9__#___7____3#83__1____#_614_759_#9____61_2#5___29_7_#__8_7____#627_____9'
    grid = Grid()
    grid.string_to_grid(str_grid)
    grid.txt_print()