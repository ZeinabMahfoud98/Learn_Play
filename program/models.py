from django.db import models

# Create your models here.

class Program(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(blank=True)
    content=models.TextField(blank=True)
    code=models.CharField(max_length=100)


class Session(models.Model):
    SESSION_TYPE_CHOICES = (
        ('virtual', 'Virtual'),
        ('central', 'Central'),
    )
    
    program = models.ForeignKey(
        "Program",
        on_delete=models.CASCADE
    )
    start_at=models.DateField()
    end_at=models.DateField()
    duration=models.CharField(max_length=50)
    cost=models.DecimalField(max_digits=5, decimal_places=2)
    count=models.CharField(max_length=100)
    note=models.TextField(blank=True)
    session_type=models.CharField(choices=SESSION_TYPE_CHOICES, max_length=10)


