from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    quantity = models.IntegerField()
    chef = models.ForeignKey("Chef", on_delete=models.CASCADE, null=True, default=None)


class Chef(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class RandomTable(models.Model):
    title = models.CharField(max_length=255)
