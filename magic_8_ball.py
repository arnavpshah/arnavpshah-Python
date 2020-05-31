from random import randint

answers = ['Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now','It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print ("hello stranger! I am the magic 8 ball")
print("**************")

def Magic8Ball():
    print("Ask me a question")
    input()

    print(answers[randint(0, len(answers) -1)])
    print("I hope that helped.")

    choice = Replay()

    if(choice == "Y"):
        Magic8Ball()
    elif(choice == "N"):
        return
    else:
        print("I did not understand! Please repeat.")
        Replay()



def Replay():
    print("Do you have another question? Type Y is yes and N if no")
    choice = input()

    return choice

Magic8Ball()
print("I hope you got your answers")
