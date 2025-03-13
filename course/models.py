from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
