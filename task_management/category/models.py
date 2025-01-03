from django.db import models

class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=100)
    tasks = models.ManyToManyField('task.TaskModel', blank=True)  

    def __str__(self):
        return self.categoryName
