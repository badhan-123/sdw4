from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField(max_length=40)
    father_name=models.TextField(default='rana')
    
class Employee(models.Model):
    date_time_field = models.DateTimeField(null=True)
    url_field = models.URLField(null=True)
    foreign_key = models.ForeignKey('self', on_delete=models.CASCADE)
    boolean_field = models.BooleanField(null=True)

class Teacher(models.Model):
    many_to_many_field = models.ManyToManyField(Student)
    duration_field = models.DurationField()
    big_auto_field = models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"Roll:{self.roll}-Name:{self.name}"