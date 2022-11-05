import re


class Student:
    def __init__(self, name, matric, grades, units):
        self._name = name
        self._matric = matric
        self._grades = grades
        self._units = units

    @property
    def name(self):
        """
        This is a getter method that gets the name of the students
        """
        return self._name

    @property
    def matric(self):
        """
        This is a getter method that gets the matric number of the students
        """
        return self._matric

    @matric.setter
    def matric(self, value):
        """
        This is a setter method that set the matric number of the student
        """
        self._matric = value

    def __rep__(self):
        return self._grades

        # return grade

    def units(self):
        return self._units

    def avg(self):
        """
        returns the average of the grades
        """
        sum = 0
        for num in self._grades:
            sum += num
        return sum/len(self._grades)

    def gpa(self):
        quality_point = 0
        grade_point = 0
        for num in self._grades:
            if num >= 70:
                grade_point = 5.0
                quality_point += self._units[self._grades.index(
                    num)] * grade_point
            elif 60 <= num <= 69:
                grade_point = 4.0
                quality_point += self._units[self._grades.index(
                    num)] * grade_point
            elif 50 <= num <= 59:
                grade_point = 3.0
                quality_point += self._units[self._grades.index(
                    num)] * grade_point
            elif 45 <= num <= 49:
                grade_point = 2.0
                quality_point += self._units[self._grades.index(
                    num)] * grade_point
            elif 40 <= num <= 44:
                grade_point = 1.0
                quality_point += self._units[self._grades.index(
                    num)] * grade_point
            else:
                grade_point = 0.0
                quality_point += self._units[self._grades.index(
                    num)] * grade_point

        total = quality_point / sum(self._units)
        if 4.50 <= total <= 5.0:
            return "Your GPA is {:.2f} You are in first class".format(total)
        elif 3.5 <= total <= 4.49:
            return "Your GPA is {:.2f} You are in second class upper".format(total)
        elif 2.5 <= total <= 3.49:
            return "Your GPA is {:.2f} You are in second class lower".format(total)
        elif 2.0 <= total <= 2.49:
            return "Your GPA is {:.2f} You are in third class".format(total)
        elif 1.5 <= total <= 1.99:
            return "Your GPA is {:.2f} You are in pass".format(total)
        else:
            return "Your GPA is {:.2f} You are not in good standing".format(total)

    def __str__(self):
        return self.gpa()

    @property
    def get_gp(self):
        """
        A getter property method that gets the gp of the student
        """
        return float("".join(re.findall('\d\.\d\d', self.gpa())))


class Science(Student):
    def __init__(self, name, matric, grades, units, course):
        super().__init__(name, matric, grades, units)
        self._course = course

    @property
    def course(self):  # This get the course of the student
        return self._course

    @course.setter  # This sets the matric number of the student
    def matric(self, value):
        self._matric = value

    def printStudentDetail(self):  # this will print the detail of the student
        return f"{self._name} with matric number {self._matric} is a student studying {self.course}"


class Medical(Student):
    def __init__(self, name, matric, grades, units, specification):
        super().__init__(name, matric, grades, units)
        self._specification = specification

    @property
    def specification(self):
        """
        This is a getter method that gets the specification of the medical student
        """
        return self._specification

    def printStudentDetail(self):
        return f'{self._name}, with matric {self._matric} number is a medical student which specialize in {self._specification}'


class Management(Student):
    def __init__(self, name, matric, grades, units, specialisation):
        super().__init__(name, matric, grades, units)
        self._specialisation = specialisation

    @property
    def specialisation(self):  # This get the course of the student
        return self._specialisation

    @specialisation.setter  # This sets the matric number of the student
    def matric(self, value):
        self._matric = value

    def printStudentDetail(self):  # this will print the detail of the student
        return f"{self._name} with matric number {self._matric} is a management student studying {self.specialisation}"


gradesForStudent_1 = [73, 61, 62, 60, 61,
                      71, 78, 58, 73, 63, 90, 45, 90, 73, 70]

gradesForStudent_2 = [53, 61, 62, 60, 91,
                      71, 78, 58, 73, 53, 90, 55, 70, 73, 70]

gradesForStudent_3 = [43, 61, 52, 60, 61,
                      61, 78, 58, 53, 63, 90, 45, 90, 53, 70]
units = [2, 3, 2, 2, 2, 2, 2, 3, 2, 3, 4, 1, 2, 3, 4]

studentOne = Student("Alli", "210407518", gradesForStudent_1, units)
studentTwo = Student("Seun", "210407514", gradesForStudent_2, units)
studentThree = Student("Tayo", "210407511", gradesForStudent_3, units)


print(studentOne.gpa())
print(studentTwo.gpa())
print(studentThree.gpa())

print("\n")
listOfGps = [studentOne.get_gp, studentTwo.get_gp, studentThree.get_gp]
print(listOfGps)
print("\n")

scienceStudent = Science(studentOne.name, studentOne.matric,
                         studentOne._grades, studentOne.units, "Microbiology")
scienceStudent.matric = "210406111"
print(scienceStudent.printStudentDetail())


managementStudent = Management(
    studentTwo.name, studentTwo.matric, studentTwo._grades, studentTwo.units, "Accounting")
managementStudent.matric = "210407999"
print(managementStudent.printStudentDetail())

medicalStudent = Medical(studentThree.name, studentThree.matric,
                         studentThree._grades, studentThree.units, 'Physiotherapy')
medicalStudent.matric = '1101029109'
print(medicalStudent.printStudentDetail())
