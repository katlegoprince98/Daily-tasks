from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    body = models.TextField(null=False, blank=False)
    dateCreated = models.DateTimeField()

    def __str__(self):
        return self.title