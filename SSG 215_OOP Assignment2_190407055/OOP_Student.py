# Hamid-Mosaku Ahmad
# 190407055
# Systems Engineering


class student:
    def __init__(self, name, matric, courses):
        self.name = name
        self.matric = matric
        self.courses = courses
        self.weights = {
            "GEG217": 2,
            "GEG219": 2,
            "SVY210": 3,
            "SSG215": 2,
            "CEG211": 3,
            "CEG213": 1,
            "MEG211": 2,
            "MEG212": 2,
            "GST201": 2,
            "CEG221": 2,
            "CEG222": 2,
            "CEG223": 1,
            "CEG224": 3,
            "CEG225": 3,
            "CEG226": 2
        }
        self.num_courses = len(courses)
        self.grades = {}
        for course in self.courses.keys():
            if self.courses[course] >= 70:
                self.grades[course] = 5
            elif self.courses[course] >= 60:
                self.grades[course] = 4
            elif self.courses[course] >= 50:
                self.grades[course] = 3
            elif self.courses[course] >= 45:
                self.grades[course] = 2
            elif self.courses[course] >= 40:
                self.grades[course] = 1
            else:
                self.grades[course] = 0

    def gpa(self):
        sum = 0
        weight = 0
        for course in self.courses.keys():
            sum += self.grades[course] * self.weights[course]
            weight += self.weights[course]
        return sum / weight

    def rank(self):
        gpa = self.gpa()
        if gpa <= 5.0 and gpa >= 4.5:
            print(self.name, "is on first class. Congratulations")
        elif gpa <= 4.5 and gpa >= 3.5:
            print(self.name, "is on second class upper. Excellent work")
        elif gpa <= 3.5 and gpa >= 2.5:
            print(self.name, "is on second class lower. Good job")
        elif gpa <= 2.5 and gpa >= 1.5:
            print(self.name, "is on third class. I know you can do better")
        else:
            print(self.name, "is on pass. Put in more effort")


class Arts(student):
    def __init__(self, name, matric, courses, major):
        super().__init__(name, matric, courses)
        self._major = major
        self.weights = {
            "ENG212": 2,
            "ENG214": 2,
            "GRM211": 3,
            "GRM213": 3,
            "GRM215": 2,
            "SPL217": 3,
            "SPL211": 1,
            "SPL219": 2,
            "PRN215": 1,
            "PRN213": 2,
            "ESY212": 1,
            "PHN218": 3,
            "PHN219": 2,
            "PHN211": 2,
            "LTR212": 1

        }

    @property
    def major(self):
        return self._major

    @major.setter
    def matric(self, value):
       self._matric = value

    def prt(self):
        print("\n{0} with matric number {1} is an Art student studying {2} ".format(
            self.name, self._matric, self._major))

student1 = student("John Paul", 190401003,
                   {"GEG217": 72,
                    "GEG219": 82,
                    "SVY210": 83,
                    "SSG215": 72,
                    "CEG211": 93,
                    "CEG213": 81,
                    "MEG211": 72,
                    "MEG212": 82,
                    "GST201": 82,
                    "CEG221": 92,
                    "CEG222": 72,
                    "CEG223": 81,
                    "CEG224": 73,
                    "CEG225": 83,
                    "CEG226": 92
                    })

student2 = student("Adamson Adebola", 190401004,
                   {"GEG217": 62,
                    "GEG219": 82,
                    "SVY210": 73,
                    "SSG215": 62,
                    "CEG211": 53,
                    "CEG213": 71,
                    "MEG211": 62,
                    "MEG212": 62,
                    "GST201": 52,
                    "CEG221": 62,
                    "CEG222": 52,
                    "CEG223": 61,
                    "CEG224": 83,
                    "CEG225": 73,
                    "CEG226": 52
                    })
student3 = student("Augustin Tomiwa", 190401080,
                   {"GEG217": 52,
                    "GEG219": 89,
                    "SVY210": 46,
                    "SSG215": 67,
                    "CEG211": 86,
                    "CEG213": 50,
                    "MEG211": 98,
                    "MEG212": 58,
                    "GST201": 93,
                    "CEG221": 65,
                    "CEG222": 87,
                    "CEG223": 46,
                    "CEG224": 75,
                    "CEG225": 57,
                    "CEG226": 66
                    })

student4 = student("Toheeb Alade", 190407025,
                   {"GEG217": 78,
                    "GEG219": 65,
                    "SVY210": 36,
                    "SSG215": 96,
                    "CEG211": 56,
                    "CEG213": 87,
                    "MEG211": 76,
                    "MEG212": 59,
                    "GST201": 30,
                    "CEG221": 67,
                    "CEG222": 95,
                    "CEG223": 49,
                    "CEG224": 58,
                    "CEG225": 79,
                    "CEG226": 69
                    })


student5 = student("Jackson Opeyemi", 190401005,
                   {"GEG217": 52,
                    "GEG219": 42,
                    "SVY210": 38,
                    "SSG215": 26,
                    "CEG211": 53,
                    "CEG213": 81,
                    "MEG211": 72,
                    "MEG212": 52,
                    "GST201": 82,
                    "CEG221": 42,
                    "CEG222": 48,
                    "CEG223": 61,
                    "CEG224": 73,
                    "CEG225": 53,
                    "CEG226": 62
                    })

artStd = Arts("Prof Ibidapo Obe", 190203002, {
    "ENG212": 54,
    "ENG214": 49,
    "GRM211": 60,
    "GRM213": 34,
    "GRM215": 72,
    "SPL217": 48,
    "SPL211": 69,
    "SPL219": 59,
    "PRN215": 80,
    "PRN213": 55,
    "ESY212": 60,
    "PHN218": 71,
    "PHN219": 58,
    "PHN211": 53,
    "LTR212": 90

},
    "English Language"

)

print("""
################################################################################
##                                 GPA LIST                                   ##
################################################################################
""")

stdlist = [student1, student2, student3, student4, student5]
gpalist = []
for student in stdlist:
    gpalist.append(student.gpa())
    gpalist.sort(reverse=True)
print(gpalist)
print()

for student in stdlist:
    student.rank()

print("\n")
artStd.prt()
