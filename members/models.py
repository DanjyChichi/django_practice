from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=7)
    age = models.PositiveIntegerField(max_length=3)
    birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'[{self.pk}] {self.name} {self.email}'