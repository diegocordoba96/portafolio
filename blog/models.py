from django.db import models
import datetime


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog/imagenes')
    fecha = models.DateTimeField(datetime.date.today)
    
    def __str__(self):
        return self.titulo