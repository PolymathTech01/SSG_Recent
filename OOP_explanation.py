# Prodedural code

def multiplybytwo(x):
    return x * 2


x = 8
print(multiplybytwo(x))


class Student:
    def __init__(self, name, matric, grades):
        self.name = name
        self.matric = matric
        self.grades = grades

    def grade_average(self):
        sum_of_grades = 0
        for num in self.grades:
            sum_of_grades += num
        return sum_of_grades/len(self.grades)

    def ambition(self, amb):
        return f'I want to be {amb}'


student_list = [Student('Fawaz', '180407068', [12, 11, 72]),
                Student('Wale', '1804070d8', [12, 11, 72]),
                Student('Kola', '1804070s8', [12, 11, 72]),
                Student('Tayo', '180407038', [12, 11, 72]),
                Student('Bose', '180407018', [12, 11, 72])]

print(student_list[4].grade_average())
print(student_list[4].ambition('Engineer'))


x = [1, 2, 3, 4]
x.append(7)
print(x)

print("alli".isalpha())
print("11".isalpha())
matric = 'AAU123'
print(matric[:3])

# constructor def __init__
# dunder init method
if not 21 > 3:
    print("I am a boy")
else:
    print("I am a girl")
