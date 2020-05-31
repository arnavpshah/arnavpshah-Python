# Python program to display Fibonnaci sequence

def recur_fibo(n):
    if n <= 1: #base condition
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
        
nterms = int(input("How many terms?\n"))

# check if the number of terms is valid 
if nterms <= 0:
    print("Please enter a positive integer.")
else:
    print("Print Fibonnaci squence:")
    for i in range(nterms):
        print(recur_fibo(i))
