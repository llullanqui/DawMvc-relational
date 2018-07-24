from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombreUsuario = models.CharField(max_length=200)
	apellidoUsuario = models.CharField(max_length=200)
	def __str__(self):
		return self.nombreUsuario + " " + self.apellidoUsuario

class Servicio(models.Model):
	nombreServicio = models.CharField(max_length=200)
	def __str__(self):
		return self.nombreServicio


class Usuario_Servicio(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.usuario) + " "+ str(self.servicio)

