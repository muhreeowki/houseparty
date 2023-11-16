from django.db.models.expressions import fields
from rest_framework import serializers
from .models import Room, models


class RoomSerializer(serializers.ModelSerializer):
    """This serializes outgoing data: data that is being sent out of the server: (GET METHOD)"""

    class Meta:
        model = Room
        fields = (
            "id",
            "code",
            "host",
            "guest_can_pause",
            "votes_to_skip",
            "created_at",
        )


class CreateRoomSerializer(serializers.ModelSerializer):
    """This serializes incoming data: data that is sent from the client side: (POST METHOD)"""

    class Meta:
        model = Room
        fields = ("guest_can_pause", "votes_to_skip")
