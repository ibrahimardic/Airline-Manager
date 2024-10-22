import pytest
from airlines.models import Airline, Aircraft


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
