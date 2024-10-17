from django.contrib import admin
from fabrics.models import Fabric

class FabricAdmin(admin.ModelAdmin):
    """
    A custom ModelAdmin class for the Fabric model.

    This class customizes the display and behavior of the Fabric model in the Django admin interface.
    """

    # Define which fields to display in the Fabric admin list view
    list_display = ['name', 'description', 'price']

    # Define fields to search in the Fabric admin interface
    search_fields = ['name', 'description']

    # Define filtering options for the Fabric admin interface
    list_filter = ['price']

# Register the Fabric model with the FabricAdmin class
admin.site.register(Fabric, FabricAdmin)

