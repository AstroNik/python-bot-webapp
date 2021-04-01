from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email