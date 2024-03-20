from django.db import models
from program.models import Session
from django.contrib.auth.models import User

class Booking(models.Model):
    title = models.CharField(max_length=100)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_time = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
