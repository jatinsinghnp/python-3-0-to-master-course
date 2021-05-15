# Variable which vlue is callable

def hellow():
    print('hellow !')


hellow()


def user_age_in_seconds():
    user_age = int(input("enter your age"))
    age_in_seconds = user_age * 365*24*60*60


print("Welcome to my age in second program")
user_age_in_seconds()

print("gode bye")


# function with args

x = int(input('enter the number 1st'))
y = int(input('enter the number 2nd'))


def sum(x, y):

    add = x+y
    print(add)


print('adding the number')
sum(x, y)
print("run success!")



# return values in function


def add(x, y):
    return x+y

result=add(5,8)
print(result)
