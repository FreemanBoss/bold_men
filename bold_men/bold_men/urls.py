from django.contrib import admin
from django.urls import path, include
from accounts.views import HomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contracts/', include('contracts.urls')),
    path('fabrics/', include('fabrics.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('measurements/', include('measurements.urls')),
    path('', HomePage.as_view(), name="home-page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
