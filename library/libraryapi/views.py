from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer, LoanSerializer
from .models import *


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    permission_classes = (user for user in queryset)
    serializer_class = LoanSerializer
