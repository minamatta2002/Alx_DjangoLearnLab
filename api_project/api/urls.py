from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # عرض قائمة الكتب فقط (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # جميع عمليات CRUD عبر ViewSet
    path('', include(router.urls)),

    # Endpoint للحصول على التوكن
    path('get-token/', obtain_auth_token, name='api_token_auth'),
]
