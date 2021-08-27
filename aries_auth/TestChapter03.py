# coding = utd-8
from Human import Human

class Student(Human):
    def __init__(self, name1, age1,school):
        super(Student,self).__init__(name1,age1)
        self.school = school
        self.__score = 0

    def marking(self,score):
        if score < 0:
            print('输入不合理')
        elif score >= 0:
            self.__score = score
        elif score >100:
            print('输入不合理')
        print(self.name+'的成绩是'+str(self.__score))

    @classmethod
    def puls_sum(cls):
        cls.sum +=1
        print(cls.sum)


stu1 = Student('冬冬', 18,'小学')
print(stu1.name,stu1.age,stu1.school)
stu1.marking(59)
print(stu1._Student__score)
Student.puls_sum()


