from app.utils.get_model_version import get_model_version
from rest_framework.response import Response
from rest_framework import status


def hello_get(self, request):
    data = {
        "message": "hello"
    }

    serializer = get_model_version('v1', 'HelloOutputModel')(data=data)

    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
