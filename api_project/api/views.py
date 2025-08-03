from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# هذا كلاس العرض فقط - ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# وهذا كلاس CRUD الكامل - ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
