from rest_framework import serializers


class HelloInputModel(serializers.Serializer):
    user = serializers.CharField(max_length=255)
