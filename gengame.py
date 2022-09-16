# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:53:17 2022
@author: Cristian Andres M. Mayuti
@license GPLV3.

"""
import pickle
import random
import os

class Game:
    def __init__(self, name):
       self.name = name.upper()
       
    def __clean_screen(self):
        if os.name in ('nt', 'dos'):
            os.system('cls')
        else:
            os.system('clear')
    
    def __gen_word(self):
        file_words = open("words.dat", "rb")
        file_words.seek(0)
        dict_words = pickle.load(file_words)
        index = random.randint(0, 99)
        return list(dict_words[index])
    
    def __control_char(self):
        while True:
            char = input("\nIngresa solo una letra: ").upper()
            if len(char) == 1:
                if char.isalpha():
                    return char
                    break
            else:
                print("\nNo ingresaste una letra. Vuelve a intentar.")
                
    def __end_game(self, name):
        self.__clean_screen()
        print("""\n\n   
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
         ========= \n\n""")
        print("\nLO SIENTO {}, HA FINALIZADO EL JUEGO Y SE ACABARON TUS OPORTUNIDADES".format(name))
        print("\nVuelve a intentar una nueva partida.")
        input("\n\nPresiona una tecla para continuar: ")
        return
    
    def run_game(self):
        __counter_error = 0
        __secret_word = "".join(self.__gen_word())
        mask_lword = []
        for i in __secret_word:
            mask_lword.append('_ ')
        while __counter_error <= 6:
            self.__clean_screen()
            mask_word = " ".join(mask_lword)
            print("\nAdivina la palabra secreta ingresando de a una letra.")
            print("\n\nTienes [ {} ] oportunidades.".format(6 - __counter_error))
            print("\n              SUERTE!!!!\n\n")
            print("\nLa palabra secreta tiene {} letras\n\n".format(len(__secret_word)))
            print(mask_word)
            char = self.__control_char()
            __find_word = 0
            for i in range(len(__secret_word)):
                if char == __secret_word[i]:
                    mask_lword[i] = char
                    __find_word +=1
            if __find_word == 0:
                print("\nNo se encuentra la letra dentro de la palabra secreta")
                print("\nVuelve a intentarlo")
                __counter_error += 1
            if __counter_error == 6:
                self.__end_game(self.name)
                self.__clean_screen()
                break
        
        
            
            
       
