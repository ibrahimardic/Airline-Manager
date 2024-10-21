from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from airlines.models import Airline, Aircraft
from airlines.api.serializers import AirlineSerializer, AircraftSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def AirlinesView(request):

    if request.method == "GET":
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(
            airlines, many=True
        )  # Ensure `many=True` for QuerySet serialization
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AirlineSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # IF not valid


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def AirCraftsView(request):
    if request.method == "GET":
        aircrafts = Aircraft.objects.all()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # IF not valid


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def RetrieveAircraftView(request, pk):

    aircraft = get_object_or_404(Aircraft, id=pk)

    if request.method == "GET":
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PATCH":
        serializer = AircraftSerializer(aircraft, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # IF not valid

    elif request.method == "DELETE":
        aircraft.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )  # No content, no data returned


@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def RetrieveAirlineView(request, pk):
    airline = get_object_or_404(Airline, id=pk)

    if request.method == "GET":

        serializer = AirlineSerializer(airline)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PATCH":

        serializer = AirlineSerializer(airline, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # IF not valid

    elif request.method == "DELETE":
        airline.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
