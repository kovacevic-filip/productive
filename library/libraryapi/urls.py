from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('login', LoginView, basename='login')
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)
router.register('loan', LoanViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('account/logout/', LogoutView.as_view(), name='logout')
]
