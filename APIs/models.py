from django.db import models


class Consult(models.Model):
    para = models.EmailField(max_length=50)
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=400)
    