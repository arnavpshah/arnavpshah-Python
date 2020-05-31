# Assignment 1

def assignment_1():
    print("Working on assignment 1\n")
    

# Assignment 2

def number_is_even(counter):
    if counter % 2 == 0:
        return True
    else:
        return False

def assignment_2():
    for counter in range (1,21):
        if number_is_even(counter):
            print("Even number:", counter)

# Assignment 3 

def assignment_3():

    sum = 1
    for counter in range(1, 6):
        sum *= counter
        print("Value of multiplication is", sum)
        
    sum = 0
    for counter in range(1,6):
        sum += counter
        print("Value of addition is", sum)
        

def main():

    assignment_1()

    assignment_2()
    
    assignment_3()

    print("End of assignments")

if __name__ == '__main__':
    main()

