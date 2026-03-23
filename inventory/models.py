# Create your models here.
# inventory/models.py

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)  # beans, machine, parts
    quantity = models.IntegerField()
    cost_price = models.FloatField()
    selling_price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name