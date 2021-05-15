#f' string string formatting  in python
#  

name ="Bob"

greeting =f"hellow ,{name}"

print(greeting)
print(greeting)


# creating template 
name="bob"
greeting="hloow,{}"
with_name=greeting.format()

with_name=greeting.format("nikhil")

with_name=greeting.format("jatin")



print(with_name)



# also kin a make long phraser



long_phraser="helow,{}.Today is {}."
formatted=long_phraser.format("tt",'tte')

print(formatted)