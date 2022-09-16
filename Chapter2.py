# Example of an if else statement
# name = 'Marry'
# password = 'swordfish'
# if name == 'Mary':
#         print('Hello Marry')
#         if password == 'swordfish':
#                 print('Access granted.')
#         else:
#                 print('Wrong password')


# Example of an elif statement
# age = 10
# if name == 'Alice':
#         print('Hi, Alice')
# elif age < 12:
#         print('Aloha, stranger')


# Example of combination of all there flow control statements
# name = 'Carol'
# age = 3000
# if name == 'Alice':
#         print('Hi, Alice')
# elif age < 12:
#         print('You are not Alice, kiddo.')
# else:
#         print('You are neither Alice nor a little kid.')


# Example of a while loop
# spam = 0
# while spam < 5:
#         print('Hello, world')
#         spam = spam + 1


# Example of a while loop + input       
# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you')


# Example of a while loop plus a break statement
# while True:
#     print('What is your name?')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you "your name"')


## Example of while loop with continue/break statement
# while True: 
#         print('Who are you?')
#         name = input()
#         if name != 'Joe':
#                 continue
#         print('Hello Joe. What is the password? It is a fish.')
#         password = input()
#         if password == 'swordfish':
#                 break
# print('Access granted.')


## Example of truthy and falsy + while loop 
# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
#     print('Done')

# #Example of basic for loop
# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')


#Another example of a for loop
# total = 0 
# for num in range(10):
#     total = total + num
# print(total)


# Example of for loop with step fuction
# for i in range(0, 11, 2):
#     print(i)


# Example of the random module in use
# import random or from random import randint

# for i in range(11):
#         print(random.randint(1, 134523452345))


# Using the System module 
# import sys
# from urllib import response
# while True: 
#         print('Type exit to exit')
#         response = input()
#         if response == 'exit':
#                 sys.exit()
#         print('You typed ' + response + '.')


# Example of a number guessing game with numbers 1 through 
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

#Guessing number game
# for guessesTaken in range(1, 7):
#         print('Take a guess.')
#         guess = int(input())

#         if guess < secretNumber:
#                 print('Your guess is too low.')
#         elif guess > secretNumber:
#                 print('Your guess is too high.')
#         else:
#                 break #This condition is the correct guess
# if guess == secretNumber:
#         print(('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!'))
# else: 
#         print('Nope. The number I was thinking of was ' + str(secretNumber))



#Rock, Paper, Scissors game
import random, sys

print('Lets play, "Rock, Paper, Scissors"')

#Vars to keep score of wins, losses and ties
wins = 0
losses = 0 
ties = 0

while True: #Main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter you move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #Used to break out of the player loop
        print('Type one of "r", "p", "s", or "q".')
    
    #Display what the player will be playing as
    if playerMove == 'r':
        print('Rock vs...')
    elif playerMove == 'p':
        print('Paper vs...')
    elif playerMove == 's':
        print('Scissors vs...')
    
    #Display what the computer chooses
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    if randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    if randomNumber == 3:
        computerMove = 's'
        print('Scissors')
    
    #Displays and record the scores overall
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r'and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p'and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r'and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p'and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's'and computerMove == 'r':
        print('You lose!')
        losses = losses + 1