class Student:
    def __init__(self,maths,science,social):
        self.maths=maths
        self.science=science
        self.social=social
    def avg(self):
        return (self.maths+self.science+self.social)/3

s=Student(90,80,70)
print(s.avg())
