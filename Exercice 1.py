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

class Affichage:
    def __init__(self, n):
        self.n = n
        self.triangle = Triangle(n)

    def afficherDeuxTriangle(self):
        for i in range(1,self.n+1):
            gauche = self.triangle.ligne_gauche(i)
            droite = self.triangle.ligne_droite(i)
            print(gauche + " " + droite)
n= int(input("saisir le nombre de lignes :"))



