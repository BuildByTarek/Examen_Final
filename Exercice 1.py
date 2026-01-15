class Triangle:
    def __init__(self, n):
        self.n = n

    def ligne_gauche(self, i):
        espaces = " " * (self.n - i)
        etoiles = "*" * i
        return espaces + etoiles
