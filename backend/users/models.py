from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
class Clients(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    addres = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        verbose_name = 'Email',
        help_text = 'Ingresa email valido'
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="el numero debe tener entre 9 y 15 digitos",
            )
        ],
        verbose_name="Numero de Telefono"
    )
    