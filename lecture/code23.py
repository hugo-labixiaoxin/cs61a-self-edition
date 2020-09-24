class Students:
    def __init__(self,number,teacher,school,cla,course):
        self.number=number
        self.teacher=teacher
        self.school=school
        self.cla=cla
        self.course=course
    def __str__(self):
        return 'number:{0},teacher:{1},school:{2},cla:{3},course:{4}'.format(self.number,self.teacher,self.school,self.cla,self.course)
class Classes:
    def __init__(self,class_number,teacher=[],student=[],school):
        self.class_number=class_number
        self.teacher=list(teacher)
        self.student=list(student)
        self.school=school
    def arrange_student(self,stu):
        self.student.append(stu)
class Courses:
    def __init__(self,course_id):
        self.course_id=course_id
class Teachers:
    def __init__(self,teacher_id):
        self.teacher_id=teacher_id
        self.responsible_classes=[]
    def assign_class(self,cla):
        self.responsible_classes.append(cla)
class Schools:
    def __init__(self,school_id):
        self.school_id=school_id
        self.teachers=[]
        self.classes=[]
    def assign_teacher(self,tea):
        self.teachers.append(tea)
    def divide_classes(self,cla):
        self.classes.append(cla)

class District:
    def __init__(self):
        self.schools=[]
    def creat_school(self,sch):
        self.schools.append(sch)
        
c=District()
for i in range(10):
    school_id='sch'+str(i+1)
    sch=Schools(school_id)
    c.creat_school(sch)
