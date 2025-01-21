

class Case(object):

    def __init__(self):
        self.value = None
        self.possibles = [i for i in range(1, 10)]

    # Savoir si la case à une valeur
    def has_value(self):
        return self.value is not None

    # Pour récuperer la valeur de la case
    def get_value(self):
        return self.value

    # Pour récuperer la liste des possibles. Si une valeur a été mise, renvoie None
    def get_possibles(self):
        return self.possibles

    # Pour modifier la valeur d'une case (enlève les possibles)
    def set_value(self, value):
        self.value = int(value)
        self.possibles = None

    # Pour actualiser les possibles d'une case
    def update_possibles(self, possibles):
        self.possibles = possibles

    # Pour savoir le nombre de possibles (si la case à une valeur, cela renvoie 0)
    def get_nb_possibles(self):
        if self.possibles is None:
            return 0
        else:
            return len(self.possibles)






