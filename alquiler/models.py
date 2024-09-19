from django.db import models

# Create your models here.

class plataforma(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    


class genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class videojuego(models.Model):
    titulo = models.CharField(max_length=50)
    plataforma= models.ForeignKey(plataforma, on_delete=models.CASCADE)
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.titulo

class alquiler(models.Model):
    cliente = models.CharField(max_length=50)
    videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)
    fecha_alquiler = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(null=True , blank=True)