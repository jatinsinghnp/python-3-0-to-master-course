

number=7

while True:
    userInput=input(" would like to play?(Y/n) :")
    if userInput=='n':
        break
    userInput=int(input("Guess our number:"))
    if  userInput==number:
        print("You guessed correctly !")
    else:
        print("Sorry,it's wrong !")