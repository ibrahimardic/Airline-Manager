from django.urls import path
from . import views


urlpatterns = [
    path('', views.AirlinesView, name="homepage"), # Root domain
    path('airline/', views.AirlinesView, name="airlines"),
    path('aircraft/', views.AirCraftsView, name="aircrafts"),
    path('airline/<str:pk>/', views.RetrieveAirlineView, name="single_airline"),
    path('aircraft/<str:pk>/', views.RetrieveAircraftView, name="single_aircraft"), 
]