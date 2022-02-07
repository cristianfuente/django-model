from django.db import models

# ModeloT TipoDocumento
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80)
    def __str__(self):
        return '{}'.format(self.nombre)

#Modelo Ciudad
class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80)
    def __str__(self):
        return '{} {}'.format(self.nombre, self.descripcion)

class Persona(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    idTipoDoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento=models.CharField(max_length=30)
    LugarResidencia= models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechanacimiento=models.CharField(max_length=30)
    email=models.CharField(max_length=150)
    telefono=models.CharField(max_length=30)
    usuario=models.CharField(max_length=40)
    password=models.CharField(max_length=30)
