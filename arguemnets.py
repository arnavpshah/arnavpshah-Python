"""
def greet(name, msg = "Good morning!"):
    This function greets to 
    the person with the provided message
    print("hello", name + ', ' +msg)
    
greet(name = "Bruce", msg = "How do you do?") # keyword arguements
greet(msg = "How do you do?", name = "Bruce") # 2 kwargs (out of order)

# 1 positional, 1 kwarg
greet("How do you do?", msg = "Bruce")
"""

def greet(*names):
    """This function greets all
    the persons in the name tuple"""
    
    #naems is a tuple with argeuments
    for name in names:
        print("Hello", name)
        
greet("Monica", "Luke", "Steve", "John")
