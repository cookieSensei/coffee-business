# expenses/models.py

from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('inventory', 'Inventory'),
        ('misc', 'Miscellaneous'),
        ('repair', 'Repair Cost'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)