from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
