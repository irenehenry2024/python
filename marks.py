import array
class student():
    def _init_(self):
        self.std_Name=str(input("Enter the Name of Student:"))
    def getMarks(self):
        self.subject1 = int(input("Enter the Marks 1:"))
        self.subject2 = int(input("Enter the Marks 2:"))
        self.subject3 = int(input("Enter the Marks 3:"))
        self.subject4 = int(input("Enter the Marks 4:"))
    def getTotal(self):
        total = self.subject1+self.subject2+self.subject3+self.subject4
        return total

obj = []
no = int(input("Enter the Number of Students Information to be Entered:"))
for i in range(no):
    obj.append(student())
    obj[i].getMarks()

for i in range(no):
    print("Name:",obj[i].std_Name)
    print("Total:",obj[i].getTotal())