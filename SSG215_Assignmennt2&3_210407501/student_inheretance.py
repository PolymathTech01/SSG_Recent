class Student:
    def __init__(self, name, units, score):
        self._name = name
        self._units = units
        self._score = score

    def name(self):
        return self._name

    def units(self):
        return self._units

    def score(self):
        return self._score

    def gpa(self):
        score_grade = []
        course_points = []
        for i in self._score:
            if i > 69:
                i = 5
            elif 59 < i < 70:
                i = 4
            elif 49 < i < 60:
                i = 3
            elif 44 < i < 50:
                i = 2
            elif 39 < i < 45:
                i = 1
            elif 1 < i < 40:
                i = 0
            score_grade.append(i)
        for grade, unit in zip(score_grade, self._units):
            course_points.append(grade * unit)
        student_gpa = sum(course_points) / sum(self._units)
        return student_gpa


n1 = "ben"
n2 = "wen"
n3 = "fen"
n4 = "ken"
n5 = "qen"

units = [2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 3, 2, 3]
g1 = [90, 89, 70, 89, 77, 79, 90, 95, 86, 70, 80, 90, 70, 89, 87]
g2 = [90, 78, 70, 89, 67, 59, 90, 79, 46, 70, 50, 90, 60, 49, 77]
g3 = [90, 69, 70, 89, 67, 59, 90, 85, 46, 70, 90, 50, 50, 59, 37]
g4 = [70, 49, 90, 59, 97, 59, 90, 55, 46, 70, 50, 90, 70, 89, 67]
g5 = [24, 39, 20, 39, 27, 39, 20, 25, 76, 40, 90, 80, 50, 59, 27]

stu_list = [
    Student(n1, units, g1),
    Student(n2, units, g2),
    Student(n3, units, g3),
    Student(n4, units, g4),
    Student(n5, units, g5),
]
gpa_list = []

# To find each student GPA
print("\n", "\n", "Each student GPA")
for student in stu_list:
    print("The GPA of", student.name(), "is", student.gpa())
    gpa_list.append(student.gpa())

# To find each student Rank
print("\n", "\n", "Each student Rank")
for student in stu_list:
    if student.gpa() > 4.4:
        print("Student", student.name(), "is on 1st class")
    elif student.gpa() < 4.4 and student.gpa() > 3.4:
        print("Student", student.name(), "is on 2nd class upper")
    elif student.gpa() < 3.4 and student.gpa() > 2.4:
        print("Student", student.name(), "is on 2nd class lower")
    elif student.gpa() < 2.4:
        print("Student", student.name(), "is on 3rd class")


# To find each student Standings
print("\n", "\n", "Each student Standings")
for student in stu_list:
    if student.gpa() < 1.5:
        print("Student", student.name(), "is not on good standings")

# GPA List
print("\n", "\n", "GPA List")
print(gpa_list)


class Law(Student):
    def __init__(self, name, units, score, cases, wins):
        super().__init__(name, units, score)
        self._cases = cases
        self._wins = wins

    # This method retuns the amount of cases the student has worked on
    def stucases(self):
        return self._cases

    # This method prints the amount of cases the student has worked on and won
    def stuwins(self):
        print("\n", "\n", self._name, "took on", self._cases, "and won", self._wins)

    # This method calcuates the case score of the student
    def score(self):
        score = (self._wins / self._cases) * 100
        return score

    # This method checks to see if the student has the minimum amount of cases won to be cerified
    def certify(self):
        if self.score() >= 70:
            print("\n", "\n", self._name, "is a certified student lawyer")
        else:
            print("\n", "\n", self._name, "does not have the required qualifications")


Law(n1, units, g1, 5, 3).certify()


class Barrista(Law):
    def __init__(self, name, units, score, cases, wins, bar):
        super().__init__(name, units, score, cases, wins)
        self._bar = bar

    # This method calcuates the bar exam score of the student
    def barscore(self):
        return self._bar

    # This method gives a prediction of the career path of the student
    def career(self):
        if (self.gpa() > 4.4) and (self._bar > 149) and (self.score()) >= 70:
            print(
                "\n",
                "\n",
                self._name,
                "has the necessary qulifications to be anything from a lawyer,senator to a judge",
            )
        else:
            print("\n", "\n", self._name, "has poor standings as a lawyer")


Barrista(n1, units, g1, 5, 4, 150).career()


################################################################
# Question 1
class Art(Student):
    def __init__(self, name, units, score, projects, exhibition):
        super().__init__(name, units, score)
        self._projects = projects
        self._exhibition = exhibition

    # This method returns the amount of projects the student has worked on
    def stuprojects(self):
        return self._projects

    # This method prints the amount of exhibition the student has worked on
    def stuexhibition(self):
        print(
            "\n",
            "\n",
            self._name,
            "worked on",
            self._projects,
            "and was showcased at ",
            self._exhibition,
            "exhibitions",
        )

    # This method calcuates the projects to exhibition ratio of the student
    def score(self):
        mark = (self._exhibition / self._projects) * 100
        print(mark)
        return mark

    # This method checks to see if the student has the minimum amount of cases won to be cerified
    def certify(self):

        if self.score() >= 70:
            print("\n", "\n", self._name, "is a certified student artist")
        else:
            print("\n", "\n", self._name, "does not have the required qualifications")


Art(n4, units, g1, 5, 3).certify()


# Quetsion 2


class Cats:
    def __init__(self, name, speed, location, color):
        self._speed = speed
        self._name = name
        self._location = location
        self._color = color

    def __call__():
        pass

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def name(self):
        return self._name

    def prt(self):
        if type(self) is Cats:
            print(
                self._name,
                "is usually found in",
                self.location,
            )
        print(
            self._name,
            "is usually found in",
            self.location,
        )


class Tigers(Cats):
    def __init__(self, name, speed, location, color, size, prey):
        super().__init__(name, speed, location, color)
        self._size = size
        self._prey = prey

    def stusize(self):
        return self._size

    def stuprey(self):
        print("\n", "\n", "Tiger", self._name, "preys on", self._prey)


Tigers("Billy", 50, "jungle", 100, "deer").stuprey()


class Leopard(Cats):
    def __init__(self, name, speed, location, color, size, prey):
        super().__init__(name, speed, location, color)
        self._size = size
        self._prey = prey

    def stusize(self):
        return self._size  # This method returns the size of the leopard

    def stuprey(self):
        print("\n", "\n", "Leopard", self._name, "preys on", self._prey)
        # This method prints the prey of the leopard


class Lion(Cats):
    def __init__(self, name, speed, location, color, size, prey):
        super().__init__(name, speed, location, color)
        self._size = size
        self._prey = prey

    def stusize(self):
        return self._size  # This method returns the size of the lion

    def stuprey(self):
        print(
            "\n", "\n", "Lion", self._name, "preys on", self._prey
        )  # This method prints the prey of the lion
        # This method prints the prey of the lion
