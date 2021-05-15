numbers=[1,2,5]
doubled=[x*2 for x in numbers]

print(doubled)


print('.......................')


friends=['jatin','sunil','slok','punky']
starts_s=[friend for friend in friends if friend.startswith("s")]
print(friends)
print(starts_s)
print(friends is starts_s)
print("friends:",id(friends),"starts_s",id(starts_s))