from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class report(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mark = models.IntegerField()
    progress = models.IntegerField()

    def __str__(self):
        return self.name