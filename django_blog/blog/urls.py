from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BlogPostViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
