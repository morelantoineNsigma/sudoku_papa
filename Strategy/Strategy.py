

class Strategy(object):

    def __init__(self, grid):
        self.effect = False
        self.grid = grid
        self.name = ""

    # Applique la stratégie à la grille donnée
    def apply(self):
        pass

    def print_name(self):
        print("using ", self.name)