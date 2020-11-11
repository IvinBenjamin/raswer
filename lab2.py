file = open("score2.txt")
line_split = [line.split() for line in file]
students = {}
topStudent = {}
topOne = 0

def getTotalPoints(firstname, lastname, addedPoints):
    for student in students:
        if firstname +" "+ lastname == student:
            point = int(students[student]) + int(addedPoints)
            students[student] = point
            return
    students[firstname+" "+lastname] = addedPoints

for content in line_split[:]:
    firstname = content[2]
    lastname = content[3]
    point = content[4]
    getTotalPoints(firstname, lastname, point)

for i in students: 
    print("Student Name: --> {} Student Points: --> {}".format(i, students[i]))
    if topOne <= students[i]:
        topOne = students[i]

for i in students: 
    if students[i] == topOne: 
        topStudent[i] = students[i]
        
for i in topStudent: 
    print("The Winner Is: --> {} Whith Points = {}".format(i, topStudent[i]))