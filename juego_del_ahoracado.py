import random
import os
import time
from art import *

from math import exp


def printf(object, more = "", score = "", art = 0, sleept = 3):
    os.system('cls')
    if art == 0:
        print('\n \n \n', object, more, score, '\n \n \n')
    else:
        print('\n \n \n')
        tprint(object) #, font='block')
        print('\n \n \n')
    time.sleep(sleept)


def character(letter):
    if letter == 'a':
        return ['a', 'á']
    if letter == 'e':
        return ['e', 'é']
    if letter == 'i':
        return ['i', 'í']
    if letter == 'o':
        return ['o', 'ó']
    if letter == 'u':
        return ['u', 'ú']
    else:
        return letter


def word():
    # Return a random word to be avaluated with the hangman function
    with open('./data/data.txt','r', encoding='utf-8') as words_list:
        words = [word[0:len(word)-1] for word in words_list]
    words_list.close()
    random_word = random.randint(0, len(words)-1)
    return words[random_word]


def score(tries, word):
    if len(word)/tries > 1:
        return 10000
    elif len(word)/tries > 0.8:
        return 10000*(1-abs((len(word)-tries)/tries))    
    else:
        return 1000*exp(len(word)-tries) 


def loop(word):
    # Creates a loop which compares word by word
    answer = ['_' for letter in range(len(word))]
    tries = 0
    while "".join(answer) != word:
        tries+=1
        os.system('cls')
        printf(" ".join(answer),art=1, sleept=0)
        letter = input('Enter a letter: ')
        letter = character(letter)
        try:
            if letter.isnumeric():
                printf('Numbers are not allowed')
            if len(letter) == 1:
                compare = [pair[0] for pair in enumerate(word) if pair[1] == letter]
                for element in compare:
                    answer[element] = letter
            else:
                printf('Into the hang game, words must be entered letter by letter')
        except AttributeError:
            compare = [pair[0] for pair in enumerate(word) if pair[1] == letter[0]]
            for element in compare:
                answer[element] = letter[0]
            compare = [pair[0] for pair in enumerate(word) if pair[1] == letter[1]]
            for element in compare:
                answer[element] = letter[1]       
    printf('Amazing, the correct word is:', word.capitalize(), f'Your score is: {score(tries, word):.4f} points')


def run():
    printf('Welcome to the hangman game ... !!!')
    printf("Hangman",art=1)
    loop(word())

    

if __name__ == '__main__':
    run()
    exit()