from django.db import models
from fabrics.models import Fabric
from orders.models import Order
from measurements.models import Measurement
from django.contrib.auth import get_user_model

User = get_user_model()

class Contract(models.Model):
    """
    Represents a summary of all the operations in terms of making an agreement with the user.

    Attributes:
        user (User): The user associated with the contract.
        fabric (ManyToManyField): The fabrics included in the contract.
        measurement (Measurement): The measurement associated with the contract.
        specification (str): Additional specifications for the contract.
        order (Order): The order associated with the contract.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contracts',
        help_text="The user associated with the contract."
    )
    fabric = models.ManyToManyField(
        Fabric,
        help_text="The fabrics included in the contract."
    )
    measurement = models.ForeignKey(
        Measurement,
        on_delete=models.CASCADE,
        help_text="The measurement associated with the contract."
    )
    specification = models.TextField(
        max_length=200,
        help_text="Additional specifications for the contract."
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='contracts',
        help_text="The order associated with the contract."
    )

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    def __str__(self):
        """
        Returns the string representation of the Contract instance.

        Returns:
            str: A string representing the user and order of the contract.
        """
        return f"{self.user} - {self.order}"

