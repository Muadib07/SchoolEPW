from django.db import models
import datetime


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, default='przedmiot_!')

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student_name = models.CharField(max_length=50, default='random_student')

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50, default='random_teacher')
    teacher_subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.teacher_name

    def get_teachers_subject(self):
        return "\n".join([m.subject_name for m in self.teacher_subject.all()])


class SchoolClass(models.Model):
    class_name = models.CharField(max_length=50, default='random_class')
    students = models.ManyToManyField(Student)
    school_class_tutor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()
    # grupy klas na sztywno (nowa class)
    # walidator do sprawdzenia czy dana kalsa zostł już stworzona w danym roku

    def __str__(self):
        return self.class_name

    def get_students(self):
        return "\n".join([m.student_name for m in self.students.all()])


class Lesson(models.Model):
    lesson_day = models.DateTimeField()
    lesson_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    current_school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('lesson_day',)

    def __str__(self):
        return self.lesson_name

    def check_day(self):
        self.lesson_day = datetime.datetime.weekday(self.lesson_day)
        if self.lesson_day == 0:
            return "Poniedziałek"
        elif self.lesson_day == 1:
            return "Wtorek"
        elif self.lesson_day == 2:
            return "Środa"
        elif self.lesson_day == 3:
            return "Czwartek"
        elif self.lesson_day == 4:
            return "Piątek"
