from Strategy.Strategy import Strategy
from Grid import Grid


class NakedPairs(Strategy):

    def __init__(self, grid):
        super().__init__(grid)
        self.name = "NakedPairs"

    def apply(self):
        structs = [self.grid.get_line, self.grid.get_col, self.grid.get_box]
        for struct in structs:
            for id in range(9):
                if struct == self.grid.get_box:
                    st = struct(id // 3, id % 3)
                else:
                    st = struct(id)
                for i in range(len(st) - 1):
                    if not st[i].has_value() and st[i].get_nb_possibles() == 2:
                        for j in range(i + 1, len(st)):
                            if not st[j].has_value() and st[j].get_nb_possibles() == 2:
                                if st[i].get_possibles() == st[j].get_possibles():
                                    for k in range(len(st)):
                                        if not st[k].has_value() and k != i and k != j:
                                            for pair_member in st[i].get_possibles():
                                                if pair_member in st[k].get_possibles():
                                                    st[k].get_possibles().remove(pair_member)
                                                    self.effect = True


