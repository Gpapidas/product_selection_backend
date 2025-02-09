from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
