from django.urls import path, include
from app.endpoints.base import base_router
from app.v1.endpoints.v1 import v1_router
from app.v2.endpoints.v2 import v2_router
urlpatterns = [
    path('', include(base_router.urls)),
    path('v1/', include(v1_router.urls)),
    path('v2/', include(v2_router.urls)),
]
