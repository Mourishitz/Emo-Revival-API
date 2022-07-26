from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(required=True)
    genre = serializers.ListField()
    tickets = serializers.IntegerField(required=False)
    sold_out = serializers.BooleanField(required=False, default=False)
    is_public = serializers.BooleanField(required=False, default=True)
    date_time = serializers.DateTimeField(required=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'genre',
            'tickets',
            'sold_out',
            'is_active',
            'is_public',
            'date_time',
        ]
