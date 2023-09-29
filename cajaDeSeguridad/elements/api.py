from .models import Secret, Identification, loginKey, card
from rest_framework  import viewsets,  permissions
from .serializers import *

class SecretViewSet(viewsets.ModelViewSet):
    queryset = Secret.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SecretSerializer

class IdentificationViewSet(viewsets.ModelViewSet):
    queryset = Identification.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IdentificationSerializer


class loginKeyViewSet(viewsets.ModelViewSet):
    queryset = loginKey.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = loginKeySerializer


class cardViewSet(viewsets.ModelViewSet):
    queryset = card.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = cardSerializer