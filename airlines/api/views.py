from rest_framework.response import Response
from rest_framework.decorators import api_view
from airlines.models import Airline, Aircraft
from airlines.api.serializers import AirlineSerializer, AircraftSerializer


@api_view(['GET'])
def AirlinesView(request):
    airlines = Airline.objects.all()
    serializer = AirlineSerializer(airlines, many=True)  # Ensure `many=True` for QuerySet serialization
    return Response(serializer.data, status=200)

@api_view(['GET'])
def AirCraftsView(request):
    aircrafts = Aircraft.objects.all()
    serializer = AircraftSerializer(aircrafts, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def RetrieveAircraftView(request, pk):
    aircraftObj = Aircraft.objects.get(id=pk)
    serializer = AircraftSerializer(aircraftObj)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def RetrieveAirlineView(request,pk):
    airlineObj = Airline.objects.get(id=pk)
    serializer = AirlineSerializer(airlineObj)
    return Response(serializer.data, status=200)