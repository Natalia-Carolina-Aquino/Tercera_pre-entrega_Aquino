from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"Hola, {self.username}"

class Knits(models.Model):
    name= models.CharField(max_length=60)
    knit_type = models.CharField(max_length=40)
    material = models. CharField (max_length=60)
    def __str__(self):
        return f"{self.name} \nTipo de Tejido: {self.knit_type} \nComposición: {self.material}"


class Yarns(models.Model):
    name = models. CharField(max_length=40)
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    width = models.IntegerField()
    material = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.name}\nMarca: {self.brand}\nColor: {self.color}\nGrosor: {self.width} mm\nMaterial: {self.material}"

class Accesories(models.Model):
    name = models.CharField(max_length=40)
    knit_type = models.CharField(max_length=40)
    material = models.CharField(max_length=60)
    width = models.CharField(max_length=20)
    length = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}\nTipo de Tejido: {self.knit_type}\nMaterial: {self.material}\nGrosor: {self.width}\nLongitud: {self.length}\nPrecio: {self.price}"