from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario=models.CharField(max_length=15)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_diag=models.DateField(verbose_name='Fecha de diagnostico')
    city=models.CharField(max_length=30,verbose_name='ciudad')
    pais=models.CharField(max_length=30)
    mail=models.EmailField('e-mail',blank=True)
    
    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)