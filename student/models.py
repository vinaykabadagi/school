from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20,null=False)
    standard=models.IntegerField(null=False,min_value=1,max_value=12)
    def __str__(self):
        return self.name
