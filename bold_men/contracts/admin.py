from django.contrib import admin
from contracts.models import Contract

class ContractAdmin(admin.ModelAdmin):
    """
    A custom ModelAdmin class for the Contract model.

    This class customizes the display and behavior of the Contract model in the Django admin interface.
    """

    # Define which fields to display in the Contract admin list view
    list_display = ['user', 'specification', 'order']

    # Define fields to search in the Contract admin interface
    search_fields = ['user__username', 'order__id']  # Search by username of associated user and order ID

    # Define filtering options for the Contract admin interface
    list_filter = ['order__created_at']  # Filter by creation date of associated order

# Register the Contract model with the ContractAdmin class
admin.site.register(Contract, ContractAdmin)

