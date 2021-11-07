from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)
router.register(r'loan', LoanViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('routes/', include('rest_framework.urls', namespace='rest_framework'))
]
