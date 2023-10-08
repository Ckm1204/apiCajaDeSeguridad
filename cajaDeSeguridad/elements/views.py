from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elements.serializers import cardSerializer
from .models import *

# Create your views here.

class CardApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        list_card = card.objects.all()
        serializador = cardSerializer(list_card, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data={
            'name':request.data.get('name'),
            'number':request.data.get('number'),
            'expirationDate':request.data.get('expirationDate'),
            'cvv':request.data.get('cvv'),
            'comment':request.data.get('comment'),
            'created_at':request.data.get('created_at')
        }
        serializador = cardSerializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,  request, pkid):
        print(pkid)
        editCard = card.objects.filter(id=pkid).update(
            name= request.data.get('name'),
            number= request.data.get('number'),
            expirationDate= request.data.get('expirationDate'),
            cvv=request.data.get('cvv'),
            comment=request.data.get('comment')
        )
        return Response(editCard, status=status.HTTP_200_OK)




    

