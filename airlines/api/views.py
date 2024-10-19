from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def AirlinesView(request):

    return Response({"message": "airlines"},status=200) 

@api_view(['GET'])
def AirCraftsView(request):

    return Response({"message": "aircrafts"}, status=200)

@api_view(['GET'])
def RetrieveAircraftView(request, pk):

    return Response(status=200)

@api_view(['GET'])
def RetrieveAirlineView(request,ok):

    return Response(status=200)