from main.models import *
from main.serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView


# Product model
# read
class GetAllProductItems(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


# create
class CreateAllProductItems(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


#  update
class UpdateAllProductItems(UpdateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializers


#  delete
class DeleteAllProductItems(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

