from django.contrib import admin
from django.urls import path, include
from .views import FabricCreateView, FabricDeleteView, FabricDetailView, FabricListView, FabricUpdateView

app_name = "fabrics"

urlpatterns = [
    path('fabrics', FabricListView.as_view(), name='fabric-list'),
    path('fabric/new/', FabricCreateView.as_view(), name='fabric-create'),
    path('fabric/<int:pk>/', FabricDetailView.as_view(), name='fabric-detail'),
    path('fabric/<int:pk>/update', FabricUpdateView.as_view(), name='fabric-update'),
    path('fabric/<int:pk>/delete', FabricDeleteView.as_view(), name='fabric-delete'),
]
