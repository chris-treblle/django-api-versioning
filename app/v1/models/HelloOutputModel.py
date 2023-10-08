from rest_framework import serializers


class HelloOutputModel(serializers.Serializer):
    message = serializers.CharField(max_length=300)
