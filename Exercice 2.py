import os
import sys
from operator import not_

from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QGridLayout, QFrame, QLineEdit, QLabel

liste =[]
scores= []

def charger():
    f= open("Resultats.txt", "r")
    for l in liste:
        l.setText(f.readline())
    f.close()

def sauver():
    f= open("Resultats.txt", "w")
    for l in liste:
        f.write(l.text()+"\n")
    f.close()

def calculer_double():
    n_txt = list[0].txt()
    if n_txt == "":
        liste[1].setText("")
        return
    if not n_txt.isdigit():
        liste[1].setText("")
        return
    n= int(n_txt)
    double = n * 2
    liste[1].setText(str(double))

app = QApplication(sys.argv)
win = QWidget()









