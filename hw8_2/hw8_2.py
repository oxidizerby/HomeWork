from decimal import Decimal


class Student(object):
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.full_name = name + ' ' + surname
        self.marks = marks

    def get_average_mark(self, subject=None):
        self._check_subject(subject)
        res = 0
        if subject is None:
            for sub in self.marks:
                res += Decimal(sum(self.marks[sub]))/len(self.marks[sub])
            res = res / len(self.marks)
        else:
            res = Decimal(sum(self.marks[subject])/len(self.marks[subject]))

        return res

    @property
    def subjects(self):
        return [*self.marks]

    def change_mark(self, subject, position, value):
        self._check_subject(subject)
        self.marks[subject][position] = value
        pass

    @staticmethod
    def compare_students(student_1, student_2, subject=None):
        res = 0
        if student_1.get_average_mark(subject) > student_2.get_average_mark(subject):
            res = 1
        elif student_1.get_average_mark(subject) < student_2.get_average_mark(subject):
            res = 2
        return res

    def _check_subject(self, subject):
        if subject is None:
            return
        for s in self.marks:
            if s == subject:
                return
        raise ValueError('Нет такого предмета!')
        pass


d1 = {'mat': [5, 4, 3], 'lit': [6, 7, 8, 4], 'fiz': [6, 7]}
d2 = {'mat': [2, 3, 3], 'lit': [8, 8, 8, 3], 'fiz': [5, 6]}

stu1 = Student('Vasya', 'Pupkin', d1)
stu2 = Student('Petr', 'Petrov', d2)
print(Student.compare_students(stu1, stu2))

