from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from arduino.models import Entrada, ESP32  # Cambié Arduino por ESP32
from arduino.serializers import EntradaSerializer
from django.utils import timezone


@api_view(['POST'])
def guardar_datos(request):
    try:
        # Validación de datos necesarios
        distancia = request.data.get("distancia")
        esp32_id = request.data.get("esp32_id")  # Cambié arduino_id por esp32_id

        if not distancia:
            return Response({"error": "El campo 'distancia' es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)

        if not esp32_id:
            return Response({"error": "El campo 'esp32_id' es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar el ESP32 al que pertenece la entrada
        try:
            esp32 = ESP32.objects.get(id=esp32_id)  # Cambié arduino por esp32
        except ESP32.DoesNotExist:  # Cambié Arduino.DoesNotExist por ESP32.DoesNotExist
            return Response({"error": "ESP32 no encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear la entrada con la fecha y hora actual usando timezone
        nueva_entrada = Entrada(
            esp32=esp32,  # Cambié arduino por esp32
            valor=distancia,
            fechaHora=timezone.now(),  # Usamos timezone.now() para manejar correctamente las zonas horarias
            procesado=False
        )
        nueva_entrada.save()

        return Response({"message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        # Manejo genérico de errores
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
