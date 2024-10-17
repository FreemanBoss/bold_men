from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Measurement(models.Model):
    """
    Represents the measurement size of a user in terms of body parts.

    Attributes:
        user (User): The user associated with the measurement.
        chest (Decimal): The chest measurement of the user.
        waist (Decimal): The waist measurement of the user.
        hip (Decimal): The hip measurement of the user.
        length (Decimal): The length measurement of the user.
        created_at (DateTime): The date and time when the measurement was created.
        updated_at (DateTime): The date and time when the measurement was last updated.
    
    Relationships:
        user (User): One-to-one relationship with the User model i.e one user for one measurement.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="The user associated with the measurement."
    )
    chest = models.DecimalField(
        max_digits=4, decimal_places=2,
        help_text="The chest measurement of the user."
    )
    waist = models.DecimalField(
        max_digits=4, decimal_places=2,
        help_text="The waist measurement of the user."
    )
    hip = models.DecimalField(
        max_digits=4, decimal_places=2,
        help_text="The hip measurement of the user."
    )
    length = models.DecimalField(
        max_digits=4, decimal_places=2,
        help_text="The length measurement of the user."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the measurement was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the measurement was last updated."
    )

    class Meta:
        verbose_name = "Measurement"
        verbose_name_plural = "Measurements"

    def __str__(self):
        """
        Returns the string representation of the Measurement instance.

        Returns:
            str: A string representing the user and creation date of the measurement.
        """
        return f"{self.user} - {self.created_at}"

    @property
    def user_measurement_info(self):
        """
        Returns a formatted string containing the user's measurements.

        Returns:
            str: A formatted string containing the user's measurements.
        """
        return f"{self.chest}-{self.waist}-{self.hip}-{self.length}"

