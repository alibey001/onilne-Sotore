from rest_framework import serializers
from .models import *



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = '__all__'