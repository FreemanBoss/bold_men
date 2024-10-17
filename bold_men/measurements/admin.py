from django.contrib import admin
from measurements.models import Measurement

class MeasurementAdmin(admin.ModelAdmin):
    """
    A custom ModelAdmin class for the Measurement model.

    This class customizes the display and behavior of the Measurement model in the Django admin interface.
    """

    # Define which fields to display in the Measurement admin list view
    list_display = ['user', 'chest', 'waist', 'hip', 'length', 'created_at', 'updated_at']

    # Define fields to search in the Measurement admin interface
    search_fields = ['user__username']  # Search by username of associated user

    # Define filtering options for the Measurement admin interface
    list_filter = ['created_at', 'updated_at']

# Register the Measurement model with the MeasurementAdmin class
admin.site.register(Measurement, MeasurementAdmin)

