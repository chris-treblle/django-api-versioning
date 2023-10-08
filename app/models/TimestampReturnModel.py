from rest_framework import serializers


class TimestampReturnModel(serializers.Serializer):
    timestamp = serializers.CharField(max_length=30)
