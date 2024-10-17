from django.contrib import admin
from django.urls import path, include
from .views import (
        MeasurementCreateView,
        MeasurementListView,
        MeasurementDetailView,
        MeasurementUpdateView,
        MeasurementDeleteView
        )
app_name = "measurements"

urlpatterns = [
    path('measurements/', MeasurementListView.as_view(), name='measurement-list'),
    path('measurement/new/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('measurement/<int:pk>/', MeasurementDetailView.as_view(), name='measurement-detail'),
    path('measurement/update', MeasurementUpdateView.as_view(), name='measurement-update'),
    path('measurement/<int:pk>/delete', MeasurementDeleteView.as_view(), name='measurement-delete'),
]
