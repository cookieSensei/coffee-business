# repairs/models.py

from django.db import models

class RepairRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    machine_type = models.CharField(max_length=200)
    issue_description = models.TextField()
    cost_estimate = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)