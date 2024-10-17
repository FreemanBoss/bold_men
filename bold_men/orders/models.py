from django.db import models
from django.contrib.auth.models import User
from payments.models import Payment
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Order(models.Model):
    status_choices = (
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
        ("Failed", "Failed")
    )

    user = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status_choices, default=status_choices[2])
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    # a payment associated with many orders
    # No paying for a single order multiple times but can pay for two order with one payment
    payment = models.ForeignKey(Payment, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} 's Order"
