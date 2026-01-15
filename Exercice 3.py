class Outils:
    def __init__(self):
        self.nombres = []

    def saisir(self):
        self.nombres=[]
        for i in range (10):
            n = int (input ("Tape l'entier numeroo" + str(i+1) +": "))
            self.nombres.append(n)

    def minimum (self):
        petit = self.nombres[0]
        for n  in self.nombres:
            if n< petit:
                petit =n
        return petit
    def maximum(self,):
        grand = self.nombres[0]
        for n in self.nombres:
            if n > grand:
                grand =n
        return grans


