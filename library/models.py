from django.db import models


# Create your models here.
class Autor(models.Model):
    name_autor = models.CharField(max_length=200)

    def __str__(self):
        return self.name_autor


class Books(models.Model):
    name_book = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_book

