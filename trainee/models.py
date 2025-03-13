from django.db import models
from  course.models import Course

# Create your models here.

class Trainee(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='trainee/image')
    isactive = models.BooleanField(default=True)
    course = models.ForeignKey(to=Course, null=True, on_delete=models.CASCADE)

