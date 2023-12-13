import time
from student import Students
from uuc import UUC
from uuc import Node
class AgeHolder:
    def __init__(self):
        self.mAge = 0

def AddAges(s, data):
    data.mAge += int(GetAge(s)) #or s.mAge
def GetAge(s):
    return s.mAge

def main():
    f = open("FakeNames.txt")
    allStudents = UUC()
    for line in f:
        fields = line.split()
        s = Students(fields[0],fields[1],fields[2],fields[3],fields[4])
        allStudents.Insert(s)
    #Traverse
    t1 = time.time()
    data = AgeHolder()
    allStudents.Traverse(AddAges, data)
    print("the ave age of all students is", data.mAge / allStudents.Size())
    f.close()
    t2 = time.time()
    print("total time traversing was", t2-t1, "seconds.")
    #Delete
    t3 = time.time()
    f = open("DeleteNames.txt")
    for line in f:
        data = line.strip()
        if not allStudents.Delete(data):
            print("error couldnt delete bc couldnt find", data)
    f.close()
    t4 = time.time()
    print("total time deleting was", t4-t3, "seconds.")
    #Retrieve
    f = open("RetrieveNames.txt")
    t5 = time.time()
    totalAge = 0
    totalCount = 0
    for line in f:
        data = line.strip()
        match = allStudents.Retrieve(data)
        if not match:
            print("error", data, "not found, cant retrieve")
        else:
            totalAge += int(allStudents.Retrieve(data).mAge)
            totalCount += 1
    f.close()
    t6 = time.time()
    print("The average age of all students in Retrieve names. txt is", totalAge / totalCount)
    print("total time retrieving was", t6-t5, "seconds.")

main()
