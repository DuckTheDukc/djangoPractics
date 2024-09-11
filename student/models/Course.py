from django.db import models
from .Student import Student
from .Teacher import Teacher
    
class Course(models.Model):
    name= models.IntegerField()
    Students=models.ManyToManyField(Student)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)