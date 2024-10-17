from django.contrib import admin
from payments.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    """
    A custom ModelAdmin class for the Payment model.

    This class customizes the display and behavior of the Payment model in the Django admin interface.
    """

    # Define which fields to display in the Payment admin list view
    list_display = ['amount', 'method', 'created_at']

    # Define fields to search in the Payment admin interface
    search_fields = ['method']

    # Define filtering options for the Payment admin interface
    list_filter = ['created_at']

# Register the Payment model with the PaymentAdmin class
admin.site.register(Payment, PaymentAdmin)

