from rest_framework import serializers


class HelloOutputModel(serializers.Serializer):
    greeting = serializers.CharField(max_length=300)
