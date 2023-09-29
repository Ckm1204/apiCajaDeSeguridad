from rest_framework import routers
from .api import SecretViewSet, IdentificationViewSet, loginKeyViewSet, cardViewSet

router = routers.DefaultRouter()

router.register('api/secrets', SecretViewSet, basename='secrets')
router.register('api/identification', IdentificationViewSet, basename='identifications')
router.register('api/loginKey', loginKeyViewSet, basename='loginKeys')
router.register('api/card', cardViewSet, basename='cards')

urlpatterns = router.urls