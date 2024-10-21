from rest_framework import serializers
from .models import Inventory

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        #fields = ['name','category','price','id'