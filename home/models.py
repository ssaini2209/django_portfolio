from django.db import models

# Create your models here.
class Data(models.Model):
    fullname = models.CharField(max_length=30)
    email= models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.fullname + " - " + self.email
