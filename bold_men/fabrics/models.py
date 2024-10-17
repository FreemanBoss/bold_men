from django.db import models

class Fabric(models.Model):
    """
    A Django model representing a type of fabric.

    Attributes:
        name (str): The name of the fabric.
        description (str): A description of the fabric.
        price (Decimal): The price of the fabric.
    """

    name = models.CharField(max_length=100, help_text="The name of the fabric.")
    description = models.TextField(help_text="A description of the fabric.")
    price = models.DecimalField(
        decimal_places=2, max_digits=10, help_text="The price of the fabric."
    )

    def __str__(self):
        """
        Returns the name of the fabric as its string representation.

        Returns:
            str: The name of the fabric.
        """
        return self.name

    def get_first_image(self):
        return self.images.first()
        


class FabricImage(models.Model):
    """
    A Django model representing images associated with fabric instances.

    Attributes:
        fabric (Fabric): The fabric instance associated with the image.
        image (ImageField): The image file uploaded for the fabric.
    """

    fabric = models.ForeignKey(
        Fabric,
        on_delete=models.CASCADE,
        help_text="The fabric instance associated with the image.",
        related_name='images'
    )
    image = models.ImageField(
        upload_to="fabrics/", help_text="The image file uploaded for the fabric."
    )

    class Meta:
        verbose_name = "Fabric Image"
        verbose_name_plural = "Fabric Images"

