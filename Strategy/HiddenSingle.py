from Strategy.Strategy import Strategy


class HiddenSingle(Strategy):

    def __init__(self, grid):
        super().__init__(grid)
        self.name = "HiddenSingle"

    def apply(self):
        for li in range(9):
            for co in range(9):
                if self.grid.get_case_nb_possibles(li, co) == 1:
                    self.grid.set_value(li, co, self.grid.get_case_possibles(li, co)[0])
                    self.effect = True

