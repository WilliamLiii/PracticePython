# number guessing game
import random


secret_number = random.randint(1,9)

guess_count = 1
while True:
    inputing = input('Please input a number between 1 to 9: ')
    if inputing == 'exit':
        break
    guess = int(inputing)
    if guess == secret_number:
        print('You got the correct number using '+ str(guess_count) + ' times')
        break
    elif guess > secret_number:
        print('Your guess is too high!')
    else:
        print('Your guess is too low!')
    guess_count += 1
