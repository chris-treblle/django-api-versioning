from rest_framework import serializers


class HelloInputModel(serializers.Serializer):
    name = serializers.CharField(max_length=255)
