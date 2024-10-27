import pytest
from airlines.models import Airline, Aircraft
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_airline_str():
    airline = Airline.objects.create(
        name="Test Airline", callsign="TEST", founded_year=2000, base_airport="TST"
    )
    assert str(airline) == "Test Airline"


@pytest.mark.django_db
def test_aircraft_str():
    airline = Airline.objects.create(
        name="Test Airline", callsign="TEST", founded_year=2000, base_airport="TST"
    )
    aircraft = Aircraft.objects.create(
        manufacturer_serial_number="1234",
        type="Test",
        model="Test 123",
        operator_airline=airline,
        number_of_engines=2,
    )
    assert str(aircraft) == "Test 123"


@pytest.mark.django_db
def test_airline_name_validation():
    airline = Airline(name="", callsign="TEST", founded_year=2000, base_airport="TST")
    with pytest.raises(ValidationError):
        airline.full_clean()


@pytest.mark.django_db
def test_aircraft_without_airline():
    with pytest.raises(IntegrityError):
        Aircraft.objects.create(
            manufacturer_serial_number="5678",
            type="Jet",
            model="Boeing 737",
            number_of_engines=2,
        )


@pytest.mark.django_db
def test_airline_creation_without_authentication():
    client = APIClient()
    url = reverse("airlines")
    data = {"name": "Unauthorized Airline", "callsign": "NOAUTH"}

    response = client.post(url, data, format="json")
    assert response.status_code == 401
