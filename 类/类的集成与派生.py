
#类的集成与派生
class OldboySchool:
    school='oldboy'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class OldboyStudent(OldboySchool):
    # school='oldboy'

    def choose_course(self):
        print('%s is choosing chourse' %self.name)

class OldboyTeacher(OldboySchool):
    # school='oldboy'

    def __init__(self, name, age, sex,level):
        # self.name = name
        # self.age = age
        # self.sex = sex
        OldboySchool.__init__(self,name,age,sex)
        self.level=level

    def score(self,stu_obj,num):
        print('%s is scoring' %self.name)
        stu_obj.score=num

# stu1=OldboyStudent('耗哥',18,'male')
# stu2=OldboyStudent('猪哥',17,'male')
stu3=OldboyStudent('帅翔',19,'female')
tea1=OldboyTeacher('egon',18,'male',10)
# print(tea1.__dict__)
tea1.score(stu3,99)
print(stu3.__dict__)
print(tea1.__dict__)
