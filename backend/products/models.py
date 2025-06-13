from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='nombre requeridp'
        )
    typeProduct = models.CharField(max_length=100)
    stock = models.IntegerField(
         validators=[
            MinValueValidator(1),    # mínimo 1
            MaxValueValidator(1000)  # máximo 1000
         ],
         verbose_name='cantidad de producto'
        )
    price =  models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.91')),
            MaxValueValidator(Decimal('9999.99'))
        ],
        verbose_name='precio producto'
    )