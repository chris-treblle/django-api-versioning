from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from app.endpoints.base import BaseSet
from .HelloGet import hello_get
from .HelloPost import hello_post


class HelloSet(viewsets.ViewSet):
    @action(detail=False, methods=['get', 'post'], url_path='hello')
    def hello(self, request):
        if request.method == 'GET':
            return hello_get(self, request)
        elif request.method == 'POST':
            return hello_post(self, request)


v1_router = DefaultRouter(trailing_slash=False)
v1_router.register(r'', BaseSet, basename='base')
v1_router.register(r'', HelloSet, basename='v1')
