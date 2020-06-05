# Password Generator

from random import randint

numbers = [1,2,3,4,5,6,7,8,9,0]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

special_characters = ['!','@','#','$','%','^','&','*','(',')']

computer1 = numbers[randint(0,9)]
computer2 = letters[randint(0, 51)]
computer3 = special_characters[randint(0, 9)]


def password_generator():
    exit_loop = True
    while (exit_loop):
        loop = str(input('\nWould you like a password? [y|n]: '))
        if (loop == 'y'):
            word_length = int(input("\nHow many charcters do you want in the password [5-15]: "))
            if (word_length == 5):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2)
            elif (word_length == 6):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1)
            elif (word_length == 7):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1)
            elif (word_length == 8):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2)
            elif (word_length == 9):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3)
            elif (word_length == 10):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3,computer2)
            elif (word_length == 11):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3,computer2,computer1)
            elif (word_length == 12):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3,computer2,computer1,computer3)
            elif (word_length == 13):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3,computer2,computer1,computer3,computer2)
            elif (word_length == 14):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3,computer2,computer1,computer3,computer2,computer1)
            elif (word_length == 15):
                print("This is your new password: ", computer1,computer2,computer3,computer3,computer2,computer1,computer1,computer2,computer3,computer2,computer1,computer3,computer2,computer1,computer3)
            else:
                print("{0} is not an integer between 5 and 15")
        else:
            print("Exiting from app")
            exit_loop = False

if __name__ == '__main__':
    password_generator()
