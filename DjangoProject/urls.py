from django.contrib import admin
from django.urls import path, include
from arduino import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', include('arduino.urls')),
    path('api/guardar_datos/', views.guardar_datos, name='guardar_datos'),
]
