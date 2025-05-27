Students = [
    ["Sakshyam", 85 , 78 , 81],
    ["Yunik", 80 , 69 , 82],
    ["Ashish", 91 , 93 , 92],
    ["Swarup" , 52 , 58 , 71]


]
for student in Students:
    name=student[0]
    marks=student[1:]
    average= sum(marks)/len(marks)
    status="pass" if average>=40 else "fail"

    print(f"Name   : {name}")
    print(f"Marks  : {marks}")
    print(f"Average: {average:.2f}")
    print(f"Status : {status}")
    print("-" * 30)
