# one things to remember input functions always carry string 

name=input("Enter your name:")
print(name)



# if u want to use the input as int or any other value u need to convert first

size_input= input("how big is your house(in square feet):")
squre_feet=int(size_input)
square_metres=squre_feet/1.8
print(square_metres)
print(f'{squre_feet} square feet is {square_metres:.2f} square meters' ) #:.2f format the  decimal 2 digit   



