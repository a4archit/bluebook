from django.db import models

# Create your models here.



class User(models.Model):
    email = models.EmailField(
        name="email",
        primary_key=True,

    )






