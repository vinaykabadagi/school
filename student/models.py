from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20,null=False)
    standard=models.IntegerField(null=False)
    def __str__(self):
        return self.name
