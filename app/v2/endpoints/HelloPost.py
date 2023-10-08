from app.utils.get_model_version import get_model_version
from rest_framework.response import Response
from rest_framework import status


def hello_post(self, request):
    serializer = get_model_version('v2', 'HelloInputModel')(data=request.data)

    if serializer.is_valid():
        name = serializer.validated_data.get("user", "")
        message = f"Hello, {name}!"

        response_data = {"greeting": message}
        response_serializer = get_model_version('v2', 'HelloOutputModel')(data=response_data)

        if response_serializer.is_valid():
            return Response(response_serializer.validated_data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
