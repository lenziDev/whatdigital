from django.db import models

# Create your models here.

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_checked = models.BooleanField(verbose_name='Checked?', default=False)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.name)