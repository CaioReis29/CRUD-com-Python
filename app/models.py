from django.db import models

# Create your models here.
class Pessoa(models.Model):
    Nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)