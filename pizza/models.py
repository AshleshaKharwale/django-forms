from django.db import models

# Create your models here.


class Size(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
