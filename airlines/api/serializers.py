from rest_framework import serializers
import uuid
from airlines.models import Airline, Aircraft


class AircraftSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    manufacturer_serial_number = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    operator_airline = serializers.PrimaryKeyRelatedField(
        queryset=Airline.objects.all()
    )
    number_of_engines = serializers.IntegerField()

    def create(self, validated_data):
        return Aircraft.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer_serial_number = validated_data.get(
            "manufacturer_serial_number", instance.manufacturer_serial_number
        )
        instance.type = validated_data.get("type", instance.type)
        instance.model = validated_data.get("model", instance.model)
        instance.operator_airline = validated_data.get(
            "operator_airline", instance.operator_airline
        )
        instance.number_of_engines = validated_data.get(
            "number_of_engines", instance.number_of_engines
        )

        instance.save()
        return instance

    class Meta:
        model = Aircraft
        fields = [
            "id",
            "manufacturer_serial_number",
            "type",
            "model",
            "operator_airline",
            "number_of_engines",
        ]

    def __str__(self):
        return self.model


class AirlineSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    name = serializers.CharField(max_length=100)
    callsign = serializers.CharField(max_length=100)
    founded_year = serializers.IntegerField()
    base_airport = serializers.CharField(max_length=3)
    aircraft_set = AircraftSerializer(many=True, read_only=True, source="aircrafts")

    def create(self, validated_data):
        return Airline.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.callsign = validated_data.get("callsign", instance.callsign)
        instance.founded_year = validated_data.get(
            "founded_year", instance.founded_year
        )
        instance.base_airport = validated_data.get(
            "base_airport", instance.base_airport
        )
        instance.save()
        return instance

    class Meta:
        model = Airline
        fields = ["id", "name", "callsign", "founded_year", "base_airport"]

    def __str__(
        self,
    ):
        return self.name
