class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate1(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res


    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.rate1()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.rate1() < other.rate1()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate1(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rate1()}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.rate1() < other.rate1()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ["Введение в програмирование"]

stud = Student('Сергей', 'Иванов', 'your_gender')
stud.courses_in_progress += ['Python', 'Git']
stud.finished_courses += ["Введение в програмирование"]

stud1 = Student('Аня', 'Кот', 'your_gender')
stud1.courses_in_progress += ['Python', 'Git']
stud1.finished_courses += ["Введение в програмирование"]

lec = Lecturer('Some', 'Buddy')
lec.courses_attached += ['Python']

lec1 = Lecturer('Жук', 'Майский')
lec1.courses_attached += ['Python']

lec2 = Lecturer('Игорь', 'Тор')
lec2.courses_attached += ['Python']

rev = Reviewer('Some', 'Buddy')
rev.courses_attached += ['Python']
rev1 = Reviewer('Вася', 'Пупкин')
rev1.courses_attached += ['Python']

rev2 = Reviewer('Зох', 'Кара')
rev2.courses_attached += ['Python']

rev.rate_hw(best_student, 'Python', 9.9)
rev1.rate_hw(stud, 'Python', 8)
rev2.rate_hw(stud1, 'Python', 7)

best_student.rate_lec(lec, 'Python', 9.9)
stud.rate_lec(lec1, 'Python', 7)
stud1.rate_lec(lec2, 'Python', 7)

stud_list = [best_student, stud, stud1]
lec_list = [lec, lec1, lec2]

def rate_course_std(course, stud_list):
    sum_ = 0
    qty_ = 0
    for std in stud_list:
        for crs in std.grades:
            std_sum_rate = std.rate_course(course)
            sum_ += std_sum_rate
            qty_ += 1
    res = round(sum_ / qty_, 2)
    return res


def rate_course_lct(course, lec_list):
    sum_ = 0
    qty_ = 0
    for lct in lec_list:
        for crs in lct.grades:
            lct_sum_rate = lct.rate_course(course)
            sum_ += lct_sum_rate
            qty_ += 1
    res = round(sum_ / qty_, 2)
    return res


print('Подсчет средней оценки за домашние задания')
print(rate_course_std('Python', stud_list))

print('подсчет средней оценки за лекции')
print(rate_course_lct('Python', lec_list))