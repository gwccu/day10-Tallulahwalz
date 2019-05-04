# File name: problemSetDay9.py
import random

wordList = ["whatup", "bird", "pink", "orange","england", "park"]
randomword = wordList[random.randint(0,4)]

characters= list(randomword)
display = list()
displaylength = len(characters)

for i in range (0, len(characters)):
  display.append("_")
print(display)

tracker = 0
userGuess = input("Guess a letter!")

while tracker <= 5:
  if userGuess in display:
    print("You already guessed this letter try again!!!")
  if userGuess in characters:
    index = characters.index(userGuess)
    display[index] = userGuess
    print(display)
    if display == randomword:
      print ('yay you got a letter')

  else:
    tracker += 1
    print(tracker)
    print ('that letter is not in this word, try again')

  if tracker == 5:
    print("You maxed out on guesses. You loose!")

  userGuess = input("Guess a letter!")

  print('Yay you guessed the word!')