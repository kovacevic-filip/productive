from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .permission import IsLibrarianUser, IsMemberUser, IsLibrarianOrMemberUser
from .serializers import AuthorSerializer, BookSerializer, LoanSerializer
from .models import *


class LoginView(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().as_view()(request=request._request)


class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == \
                "destroy":
            permission_classes = [IsLibrarianUser]

        return [permission() for permission in permission_classes]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == \
                "destroy":
            permission_classes = [IsLibrarianUser]
        elif self.action == 'list':
            permission_classes = [IsLibrarianOrMemberUser]

        return [permission() for permission in permission_classes]


class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [TokenAuthentication]
    def get_permissions(self):
        permission_classes = []
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == \
                "destroy":
            permission_classes = [IsLibrarianUser]
        elif self.action == 'list':
            permission_classes = [IsMemberUser]

        return [permission() for permission in permission_classes]


class Catalog(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
