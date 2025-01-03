from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('category.TaskCategory', blank=True)  # Use string reference

    def __str__(self):
        return self.taskTitle
