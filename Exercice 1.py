class Triangle:
    def __init__(self, n):
        self.n = n

    def ligne_gauche(self, i):
        espaces = " " * (self.n - i)
        etoiles = "*" * i
        return espaces + etoiles
    def ligne_droite(self,i):
        etoiles = "*" * i
        espaces = " " * (self.n - i)
        return etoiles + espaces

