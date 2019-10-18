#guessing game
import random
print('Hi, what is your name?')
name = input()
print('Ok, ' + name + ' it is time to play.')
print('Guess a number between 1 and 56')
compNum = random.randint(1, 56)
for guesses in range(1, 12):
    print('take a guess')
    guess = int(input())

    if guess < compNum:
        print('Higher')
    elif guess > compNum:
        print('Lower')
    else:
        break 
if guess == compNum:
    print('yaya, ' + name + ' only ' + str(guesses) + ' tries.')
else:
    print('nope, I had ' + str(compNum))




