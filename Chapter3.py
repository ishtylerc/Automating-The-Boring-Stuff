# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello, there.')

# hello()    


""" def intro_message(name, age, gender):
    print('Hello, ' + name + 'you are ' + age + 'and you are a ' + gender + '.')

intro_message('Alice ', '31 ', 'Female')
intro_message('John ', '25 ', 'Male')    """

import random

def magic3Ball(ballNumber):
    if ballNumber == 1:
        return 'It is certain'
    elif ballNumber == 2:
        return 'Ehh try again :/'
    elif ballNumber == 3:
        return 'You are out of luck'
    
r = random.randint(1, 3)
fortune = magic3Ball(r)

print(fortune)