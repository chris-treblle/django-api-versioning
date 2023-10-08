from datetime import datetime
from app.utils.get_model_version import get_model_version
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from rest_framework import status


class BaseSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def ping(self, request):
        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        timestamp_serializer = get_model_version('v1', 'TimestampReturnModel')(data=data)

        if timestamp_serializer.is_valid():
            return Response(timestamp_serializer.data)
        else:
            return Response(timestamp_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


base_router = DefaultRouter()
base_router.register(r'', BaseSet, basename='base')
