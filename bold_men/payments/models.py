from django.db import models

class Payment(models.Model):
    """
    A Django model representing a payment transaction.

    Attributes:
        amount (Decimal): The amount of the payment.
        method (str): The payment method used (e.g., credit card, PayPal).
        created_at (DateTime): The date and time when the payment was created.
    """

    amount = models.DecimalField(
        decimal_places=2, max_digits=10,
        help_text="The amount of the payment."
    )
    method = models.CharField(
        max_length=255,
        help_text="The payment method used (e.g., credit card, PayPal)."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True,
        help_text="The date and time when the payment was created."
    )

