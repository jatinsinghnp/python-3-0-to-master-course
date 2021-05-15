friends_ages = {"jatin": 18, "sunil": 3, "slok": 37}

print(friends_ages['jatin'])


print('.................')


friends_ages = {"jatin": 18, "sunil": 19, "slok": 19}

friends_ages['jatin'] = 19

print(friends_ages['jatin'])


print('.............................')


friends = [
    {
        "name": "jatin", "age": 24

    },
    {
        "name": "sunil", "age": 100
    },
    {
        "name": "punky", "age": 400
    }
]


print(friends[1]["name"])


# for loop + dict


students_attendance = {"Ram": 96, "Bob": 80, "hari": 100}


for student, attendance in students_attendance.items():
    print(f"{student}:{students_attendance[student]}")


# check in dectionary
if "Bob" in students_attendance:
    print({f"Bob:{students_attendance['Bob']}"})
else:
    print("Bob is not a student")