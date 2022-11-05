# Hamid-Mosaku Ahmad
# 190407055
# Systems Engineering


from OOP_Student import student


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

#The new class that is a child of the Student class
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


#The second generation inherited class
class CreativeArts(Arts):
    def __init__(self, name, matric, courses, major):
        super().__init__(name, matric, courses, major)

    def spch(self):
        print("May you all succeed in all your endeavour.")

ca_std = CreativeArts("Zainab Yusuf", 190202017, {
    "ENG212": 60,
    "ENG214": 93,
    "GRM211": 67,
    "GRM213": 41,
    "GRM215": 87,
    "SPL217": 48,
    "SPL211": 58,
    "SPL219": 99,
    "PRN215": 31,
    "PRN213": 26,
    "ESY212": 73,
    "PHN218": 81,
    "PHN219": 58,
    "PHN211": 53,
    "LTR212": 48

}, "Creative Arts")

ca_std.prt()
ca_std.spch()

# Another instance of the second generation inherited class
class CreativeArts(Arts):
    def __init__(self, name, matric, courses, major):
        super().__init__(name, matric, courses, major)

    def spch(self):
        print("May you all succeed in all your endeavour.")


ca_std = CreativeArts("Lady Maria", 190202017, {
    "ENG212": 50,
    "ENG214": 43,
    "GRM211": 47,
    "GRM213": 51,
    "GRM215": 67,
    "SPL217": 48,
    "SPL211": 58,
    "SPL219": 59,
    "PRN215": 61,
    "PRN213": 56,
    "ESY212": 73,
    "PHN218": 71,
    "PHN219": 58,
    "PHN211": 53,
    "LTR212": 48

}, "Creative Arts")

ca_std.prt()
ca_std.spch()


# 
class Law(student):
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
        print("\n{0} with matric number {1} is an Law student studying {2} ".format(
            self.name, self._matric, self._major))


class Law(Law):
    def __init__(self, name, matric, courses, major):
        super().__init__(name, matric, courses, major)

    def spch(self):
        print("May you all succeed in all your endeavour.")


ca_std = Law("Aminah Obalakun", 190202017, {
    "ENG212": 50,
    "ENG214": 43,
    "GRM211": 47,
    "GRM213": 51,
    "GRM215": 67,
    "SPL217": 48,
    "SPL211": 58,
    "SPL219": 59,
    "PRN215": 61,
    "PRN213": 56,
    "ESY212": 73,
    "PHN218": 71,
    "PHN219": 58,
    "PHN211": 53,
    "LTR212": 48

}, "Law")

ca_std.prt()
ca_std.spch()
