from rest_framework import serializers
from .models import Secret, Identification, loginKey, card


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('id', 'name', 'secret', 'key', 'comment', 'created_at')
        read_only_fields = ('created_at',)

class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields = ('id', 'name', 'number', 'fullName', 'birthDate', 'expeditionDate', 'comment', 'created_at')
        read_only_fields = ('created_at',)
        
class loginKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = loginKey
        fields = ('id', 'name', 'website', 'username', 'email', 'password', 'comment', 'created_at')
        read_only_fields = ('created_at',)
        

class cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = card
        fields = ('id', 'name', 'number', 'expirationDate', 'cvv', 'comment', 'created_at')
        read_only_fields = ('created_at',)