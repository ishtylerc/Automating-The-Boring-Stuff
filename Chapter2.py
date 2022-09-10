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

while True: 
        print('Who are you?')
        name = input()
        if name != 'Joe':
                continue
        print('Hello Joe. What is the password? It is a fish.')
        password=input()
        if password == 'swordfish':
                break
print('Access granted.')