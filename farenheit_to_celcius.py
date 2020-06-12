#Convert F to C: F = 9/5 * C + 32
#Convert C to F: C = (F - 32) * 5/9

def farenheit_to_celsius():
    answer = int(input("How many °F do you have and we will turn it to °C: "))
    x = answer - 32
    print(x * 5/9 , "celsius")
farenheit_to_celsius()
