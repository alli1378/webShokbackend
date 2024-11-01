from django.forms.models import fields_for_model
from rest_framework import serializers
from Product.models import Product,Special
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','thumbnail','title']
class ProductSerializer(serializers.ModelSerializer):
    brand=BrandSerializer()
    class Meta:
        model=Product
        fields=['id','price','thumbnail','title','description','brand','seller','color']
class SpechialSerializer(serializers.ModelSerializer):
    # brand=BrandSerializer()
    class Meta:
        model=Special
        fields=['sizepants','sizeshose','sizeshirt','price','count','seller_2','product','id']
  
class Spechial2Serializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=Special
        fields=['sizepants','sizeshose','sizeshirt','price','count','seller_2','product','id']
     