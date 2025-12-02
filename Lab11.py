import os
import matplotlib.pyplot as plt

#s : name and 3num ids
#a : name, p val, 5num id. q 8 4num. up to 1000


students = {}
with open("data/students.txt") as my_file:
    for line in my_file:
        line = line.strip()
        s_id = line[:3]
        s_name = line[3:]
        students[s_id] = s_name


assignments = {}
with open("data/assignments.txt") as my_file:
    line = my_file.readlines()

i = 0
while i < len(line):
    name = line[i].strip()

    if name == "":
        i+=1
        continue

    a_id = line[i+1].strip()
    point = int(line[i+2].strip())
    assignments[a_id] = {
        "name": name,
        "point": point
    }
    i += 3
total_p = 0
for a_id in assignments:
    total_p += assignments[a_id]["point"]
points = {}
score  = {}
for i in students:
    points[i] = 0
for i in assignments:
    score[i] = []

for filename in os.listdir("data/submissions"):
    fp = os.path.join("data/submissions", filename)
    with open(fp) as my_file:
        l = my_file.readline().strip()
        if l == "":
            continue
        sect = l.split("|")
        if len(sect) != 3:
            continue
        s_id = sect[0]
        a_id = sect[1]
        percent = int(sect[2])

    assigned = assignments[a_id]["point"]
    got = assigned * (percent/100)
    points[s_id] += got
    score[a_id].append(percent)

menu =  print("1. Student grade\n"
              "2. Assignment statistics\n"
              "3. Assignment graph\n")
option = int(input("\nEnter your selection: "))

if option == 1:
    s_name = input("What is the student's name: ")
    s_id = ""
    for i in students:
        if students[i] == s_name:
            s_id = i
    if s_id == "":
        print("Student not found")
    else:
        percent = (points[s_id]/total_p) * 100
        rpercent = round(percent)
        print(f"{rpercent}%")

elif option == 2:
    a_name = input("What is the assignment name: ")
    a_id = ""
    for i in assignments:
        if assignments[i]["name"] == a_name:
            a_id = i
    if a_id == "":
        print("Assignment not found")
    else:
        scores = score[a_id]
        mini = min(scores)
        maxi = max(scores)
        total = 0
        for i in scores:
            total += i
        avg = int(total/len(scores))
        print(f"Min: {mini}%\n"
              f"Avg: {avg}%\n"
              f"Max: {maxi}%")

elif option == 3:
    a_name = input("What is the assignment name: ")
    a_id = ""
    for i in assignments:
        if assignments[i]["name"] == a_name:
            a_id = i
    if a_id == "":
        print("Assignment not found")
    else:
        scores = score[a_id]
        plt.hist(scores)
        plt.show()

