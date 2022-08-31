# This program says hellow and asks for your name.

#printer introductory statement
print('Hello, world')
print('What is your name?')

#creates a variable for the name requested
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
#prints number of characters in the input text
print(len(myName))

#takes input and turns it to a number in order to incement by 1. Then take updated int. and turns it to a str to be concatonated with the other text
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')