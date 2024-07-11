# word puzzle game
# 1. create a list of words
# 2. pick a random word from the list
# 3. ask the user to guess the word
# 4. if the user guesses the word, tell them they won
# 5. if the user guesses the wrong letter, tell them they lost

# import random

# list_of_words = ['pizza','dance','food','airport','plant','flower','book','cat','clothes','river','tree','zoo']
# word = random.choice(list_of_words)
# print(word)
# ask_user = input('Guess the word : ')
# if ask_user == word:
#     print('You won')
# else :
#     print('You lost')


from random import *

# spelling = ['t','r','e','e']
# extra_letter = ['w','y','u','s','f','a']
# word = spelling + extra_letter
# shuffle(word)
# print(word)
# guess = input('Guess the word : ')
# guess_list = list(guess)
# if guess_list == spelling:
#     print('You Won')
# else :
#     print('You Lost')

import random
spelling = 'mango' 
extra_letter = 'abcdefghijklmnopqrstuvwxyz'
length = len(spelling)*1
for i in range(length):
    selected = random.shuffle(extra_letter)
# selected = random.sample(extra_letter,len(spelling)*1)
word = list(spelling) + selected

# for i in range(len(spelling)*2):
#     if len(word) < len(spelling):
#         word.append(spelling[i])
#     else:
#         word.append(extra_letter[i])

shuffle(word)
print(word)
guess = input('Guess the word : ')
# guess_list = list(guess)
if guess == spelling:
    print('You Won')
else:
    print('You Lost')