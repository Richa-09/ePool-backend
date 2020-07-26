from django.urls import path, include
from rest_framework import routers
from .views import OfferViewSet, UserViewSet, RequestViewSet, UserFromTokenViewSet

router = routers.DefaultRouter()
router.register('offers', OfferViewSet)
router.register('requests', RequestViewSet)
router.register('users', UserViewSet)
router.register('user-from-token', UserFromTokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
