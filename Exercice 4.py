class Voiture:
    def __init__(self,marque, annee):
        self.marque = marque
        self.annee = annee

    def fonctionne(self):
        print(f"La voiture {self.marque} fonctinne bien")
