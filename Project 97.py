



from ast import Break
import numbers
from random import Random, random


print("Number guessing game")
print("Guess a number between 1 to 9: ")

Guess = input("Enter your guess: ")

random = (1,2,3,4,5,6,7,8,9)

if(Guess == random):
    print("You Won!!")
else:
    print("You Lose!!")
     