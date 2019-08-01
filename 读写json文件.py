import json
class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'sex': std.sex,
    }
s = Student('zhangsan',20,'male')
print(json.dumps(s, default=student2dict))
f = open("E:\\8月1日工作\\test.json","w",encoding="UTF-8")
f.write(json.dumps(s, default=student2dict))
f.close

