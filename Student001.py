class Student:
    def __init__(self, name, matric, grades):
        if not matric[:3].isalpha():
            raise ValueError(
                f'"{matric}" is not a proper matriculation number')
        if not (matric[3:].isdigit() and int(matric[3:]) <= 999):
            raise ValueError(
                f'"{matric}" is not a proper matriculation number')
        self._matric = matric
        self._name = name
        self._grades = grades

    def __call__(self):
        return f"I am a student and my name is {self._name}"

    @classmethod
    def createByName(cls, nameStr):
        ss = cls(nameStr, 'MMM000', [0]*6)
        return ss

    @property
    def matric(self):
        return self._matric

    @matric.setter
    def matric(self, value):
        self._matric = value

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value):
        self._grades = value

    def name(self):
        return self._name

    def avg(self):
        sum = 0
        for num in self._grades:
            sum += num
        return sum/len(self._grades)

    def prt(self):
        if type(self) is Student:
            print(self._name,  "with matric", self._matric,
                  ' is an ordinary student')
        print('His term grades are', self._grades)


class Athletic(Student):
    def __init__(self, name, matric, grades, specSport):
        super().__init__(name, matric, grades)
        self._specSport = specSport

    @property
    def specSport(self):
        return self._specSport

    @specSport.setter
    def matric(self, value):
        self._specSport = value

    def prt(self):
        print(self._name, "with matric", self._matric,
              ' is an athletic student playing', self._specSport)
        super().prt()


class Engr(Student):
    def __init__(self, name, matric, grades, indAttach):
        super().__init__(name, matric, grades)
        self._indAttach = indAttach

    @property
    def indAttach(self):
        return self._indAttach

    @indAttach.setter
    def matric(self, value):
        self._indAttach = value

    def prt(self):
        print(self._name, "with matric", self._matric,
              'is an engineering student attached to', self._indAttach)
        super().prt()

    def __call__(self):
        super().__call__()
        return "Also an engineering student doing IT at, ", self._indAttach


class Medical(Student):
    def __init__(self, name, matric, grades, prstPost):
        super().__init__(name, matric, grades)
        self._prstPost = prstPost

    @property
    def prstPost(self):
        return self._prstPost

    @prstPost.setter
    def matric(self, value):
        self._prstPost = value

    def prt(self):
        print(self._name, "with matric", self._matric,
              'is a medical student posted to', self._prstPost)
        super().prt()


class Management(Student):
    def __init__(self, name, matric, grades, specification, favorite_course):
        super().__init__(name, matric, grades)
        self._specification = specification
        self._favorite_course = favorite_course

    @property
    def specification(self):
        return self._specification

    @property
    def favorite_course(self):
        return self._favorite_course

    def prt(self):
        print(self._name, "with matric", self._matric,
              'is a management student which specialize in ', self._specification)
        super().prt()


g1 = [50, 56, 90, 92, 93, 45]
g2 = [20, 30, 46, 90, 80, 76]
g3 = [40, 87, 67, 34, 35, 13]
g4 = [32, 45, 65, 45, 87, 29]
g5 = [50, 56, 90, 92, 93, 45]
g6 = [20, 30, 46, 90, 80, 76]
g8 = [40, 87, 67, 34, 35, 13]
g7 = [32, 45, 65, 45, 87, 29]
n1 = "Asubiaro Ojukwu"
n2 = "Maroko Sango"
n3 = "Owambe Kilode"
n4 = "Miofe Mode"
m1 = "SSG123"
m2 = "MEC105"
m3 = "ELC001"
m4 = "IOT001"
n5 = "Kako Nwata"
n6 = "Tukto Yaktuk"
n7 = "Kowambe Kilode"
n8 = "Auwa Imode"
m5 = "AAA123"
m6 = "FST105"
m7 = "MKI001"
m8 = "ABC001"
stdLst = [Student(n1, m1, g1),
          Student(n2, m2, g2),
          Student(n3, m3, g3),
          Student(n4, m4, g4),
          Engr(n5, m5, g5, "Ove Arup"),
          Medical(n6, m6, g6, 'Surgery'),
          Athletic(n7, m7, g7, 'Badmington'),
          Student(n8, m8, g8)]
pass
stdLst[4]()
sNew = Student.createByName("Okwezilieze Nwodo")
sNew.matric = 'SSG234'
mm = stdLst[0].matric
sNew.grades = [45, 56, 25, 67, 88, 99]
stdLst.append(sNew)
namesLst = {}
for std in stdLst:
    print(std())
    namesLst[std.avg()] = std.name()
print(namesLst)
for keys in sorted(namesLst.keys()):
    print(f"{keys:.2f}, {namesLst[keys]}")
nuSubj = len(stdLst[0].grades)
classAvg = [0]*nuSubj
print(f"The Class Average is {classAvg[0]:.2f}")
for std in stdLst:
    for i in range(nuSubj):
        classAvg[i] += std.grades[i]
for i in range(nuSubj):
    classAvg[i] /= len(stdLst)
    print(f"The Class Average is {classAvg[i]:.2f}")
for std in stdLst:
    std.prt()
