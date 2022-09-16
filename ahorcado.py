# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: Cristian Andres M. Mayuti
@license GPLV3.

"""
from gengame import Game
name = ""

def game(name):
   game = Game(name)
   game.run_game()

def repeat_game(name):
    while True:
        repeat = input(
            "¿Quisieras jugar otra partida? - Ingresa una S (Si) o N (No): ")
        if repeat.lower() == "s":
            game(name)
        elif repeat.lower() == "n":
            break
        else:
            print("Recuerda que debes ingresar una letra 'S' o 'N'")

def start():
    print("\n.::BIENVENIDO/A AL JUEGO DEL AHORCADO::.\n")
    
    name = input("\nIngresa tu nombre: ")
    
    print("\nHola {}".format(name))
    
    while True:
        start_game = input("¿¡Comenzamos a Jugar el Ahorcado!? - Ingresa una S (Si) o N (No): ")
    
        if start_game.lower() == "s":
            game(name)
            repeat_game(name)
            print("\nEspero te hayas divertido!!!")
            break
        elif start_game.lower() == "n":
            break
        else:
            print("Recuerda que debes ingresar una letra 'S' o 'N'")
    print("\nHasta Pronto!!!") 


if __name__ == "__main__":
    start()
