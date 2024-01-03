from django.db import models

class Staff (models.Model):

    class Roles(models.TextChoices):
        CEO = "C", "مدیر عامل"
        EXPERT = "E", "کارشناس"
        MANAGER = "M", "مدیر"


    first_name = models.CharField(default = '', max_length=256)
    last_name = models.CharField(default = '', max_length=256)
    salary = models.IntegerField(default=1000)
    role = models.CharField(
        max_length=1,
        choices=Roles.choices,
        default=Roles.CEO,
    )


