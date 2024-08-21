from django.db import models

from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    date = models.DateField()

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    lesson_name = models.CharField(max_length=100)
    date = models.DateField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

class GroupStudent(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_status = models.BooleanField(default=True)
    reg_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Contract(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    contract_number = models.IntegerField()
    add_date = models.DateField()
    end_date = models.DateField()