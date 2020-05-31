# Program to display th Fibonacci sequence to the n-th term

nterms = int(input("How many terms?\n"))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer.")
elif nterms == 1:
    print("Fibonnaci sequence", nterms, ":")
    print(n1)
else:
    print("Print Fibonnaci sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update value
        n1 = n2
        n2 = nth
        count += 1
