from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BlogPostViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path
from .views import PostListCreateView, PostDetailView, CategoryListView

urlpatterns = [
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
]
