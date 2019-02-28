##This is a number guessing game
from random import randint
print("I'm thinking of a number between 1 and 100")

secret_number = randint(1, 100)
#this line prints the guess, but that defeats the purpose.  Throw a # in front of it to hide the secret_number
#print(secret_number)
while True:
  your_guess = int(input("What is your guess? \n"))
  print
  if your_guess < secret_number:
      print("Guess is too low")
      
  elif your_guess > secret_number:
      print("Guess is too high ") 
      
  else:
      print ("That's it. Great guess!")
      break
  print
