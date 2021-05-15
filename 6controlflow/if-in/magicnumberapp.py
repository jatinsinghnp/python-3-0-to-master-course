number=7
userInput=input("Enter 'y' if you would like to play :")

if  userInput in("y","Y"):
    userInput=int(input("Guess our number:"))
    if  userInput==number:
        print("You guessed correctly !")
    else:
        print("Sorry,it's wrong !")