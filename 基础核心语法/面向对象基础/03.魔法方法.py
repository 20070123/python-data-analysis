class Stu:
    def __init__(self, name,score,gender):
        self.name = name
        self.score = score
        self.gender = gender

    def __str__(self):
        return f"学生{self.name}"

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.gender > other.gender

stu1=Stu("张三","99","男")
stu2=Stu("翠花","99","女")

print(stu1)





