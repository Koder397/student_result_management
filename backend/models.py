from django.db import models


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)

    roll_number = models.CharField(max_length=255)

    name = models.CharField(max_length=255)

    dob = models.DateField()

    def __str__(self):
        return self.roll_number

    class Meta:
        db_table = 'student'


class MarkList(models.Model):
    id = models.BigAutoField(primary_key=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    subject_name = models.CharField(max_length=255)

    mark = models.IntegerField()

    def __str__(self):
        return "Subject No.{}".format(self.id)

    class Meta:
        db_table = 'marklist'

