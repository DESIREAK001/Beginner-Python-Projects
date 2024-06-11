#this is a Guess the Number game
#import random
import random

#initialise the number of guesses taken to 0
guessesTaken = 0

#prompt the player to enter their name
player = input("Hello! What is your name?\n")

#give a range for the values to be guessed
number = random.randint(1, 20)
print(f"Well, {player}, I am thinking of a number between 1 and 20.")

#create a loop that allows a player to have 6 guesses
for guessesTaken in range (6):
  #prompt the player to enter their guess
  guess = int(input("Take a guess.\n"))

  #add conditions for when the answer is wrong
  if (guess > number):
    print("Your guess is too high!")

  if (guess < number):
    print("Your guess is too low!")

  #condition if the guess is the same as the number of the computer
  if (guess == number):
    break

if (guess == number):
  guessesTaken = str(guessesTaken + 1)
  print(f"Good job, {player}! You have guessed my number in {guessesTaken} guesses")

if (guess != number):
  number = str(number)
  print(f"Nope. The number i was thinking of was {number}.")


