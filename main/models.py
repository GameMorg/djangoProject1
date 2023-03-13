from django.db import models


class Main(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()

    def __str__(self):
        return self.field1


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)


















