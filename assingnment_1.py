# Assignment 1

def assignment_1():

    for counter in range (1,11):
        print (counter)


# Assignment 2

def assignment_2():
    goOn = True
    number = 0
    half = 0

    while(goOn):
        print ("Please type a whole number and if you want to end please type 0:")

        number = input() # input() method automatically assigns string in variable

        print(type(number))

        if (number == '0'):
            goOn = False

        else:
            half = number//2
            print ("Number is ", number, "half is", half)

def main():

    assignment_1()

    assignment_2()

    print("End of assignments")

if __name__ == '__main__':
    main()
