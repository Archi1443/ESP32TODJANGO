from django.urls import path
from rest_framework import routers
from arduino.viewsets import ArduinoViewSet, ClienteViewSet, EntradaViewSet, SalidaViewSet
from arduino import views
route = routers.SimpleRouter()
route.register(r'arduino', ArduinoViewSet)
route.register(r'cliente', ClienteViewSet)
route.register(r'entrada', EntradaViewSet)
route.register(r'salida', SalidaViewSet)
urlpatterns = route.urls

