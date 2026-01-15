import os
import sys
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








