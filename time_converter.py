"""

Make a python program that asks the user for a choice of 
what they want to convert (4 choices in a menu style).
The options will be minutes to seconds, seconds to minutes, hours to minutes. 
And hours to days. Should output as "x number of days and y number of hours"

"""



def Units_Changer():  
    
    print("Type 1 to convert minutes to seconds")
    print("Type 2 to convert seconds to minutes")
    print("Type 3 to convert hours to minutes")
    print("Type 4 to convert hours to days")
    
    choice = int(input())
    
    def minutes_to_seconds():
    
        min_to_sec = int(input("Name a number of minutes and I will convert it to seconds:"))
    
        if min_to_sec == 0:
            print("You have to use a number greater than one")
        else:
            print(min_to_sec*60 , "seconds")
    
    def seconds_to_minutes():
    
        sec_to_min = int(input("Name a number of seconds and I will convert it to minutes:"))
    
        if sec_to_min == 0:
            print("You have to use a number greater than one")
        else:
            print(sec_to_min/60 , "minutes")

    def hours_to_minutes():
    
        hr_to_min = int(input("Name a number of hours and I will convert it to minutes:"))
    
        if hr_to_min == 0:
            print("You have to use a number greater than one")
        else:
            print(hr_to_min*60 , "minutes")
    
    def hours_to_days():
    
        hr_to_d = int(input("Name a number of hours and I will convert it to days:"))
    
        if hr_to_d == 0:
            print("You have to use a number greater than one")
        else:
            print(hr_to_d/24 , "days")

    if choice == 1:
        minutes_to_seconds()
    elif choice == 2:
        seconds_to_minutes()
    elif choice == 3:
        hours_to_days()
    elif choice == 4:
        days_to_hours()
    else:
        print("That is not a valid input")
        
    
Units_Changer()

