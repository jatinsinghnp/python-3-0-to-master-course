friends=["jatin","sunil","punky"]
for friend in friends:
   print(f'{friend} is my friends')

print('...........................')
for  friends in range(4):
   print(f'{friend} is my friends')
    


# let calculate the average of  given grades using for loop try not to look at solution first try by yourself


grades=[35,67,100,100]
total=0
amount=len(grades)  #len() is a function which calculate length of the grades

for grade in grades:
    total=total+grade
    print(total/amount)

