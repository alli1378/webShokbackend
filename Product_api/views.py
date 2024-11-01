from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import AllowAny,IsAuthenticated 
from rest_framework.generics import (CreateAPIView
                                    ,RetrieveAPIView
                                    ,ListAPIView
                                    ,RetrieveDestroyAPIView
                                    ,RetrieveUpdateAPIView
                                    )
from .serializers import (ProductSerializer,
                        BrandSerializer,
                        SpechialSerializer,
                        Spechial2Serializer)
from Product.models import Brand, Product, Special
# Create your views here.
class ProductSpecialList(ListAPIView):
    # queryset=Product.objects.published()
    serializer_class=SpechialSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        pro=get_object_or_404(Product,pk=pk)
        special=pro.product.all()
        return special
class ProductDetail(RetrieveAPIView):
    # queryset=Product.objects.published()
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        pro=Product.objects.filter(pk=pk)
        # spechial=pro.product.all()
        return pro

class ProductList(ListAPIView):
    queryset=Product.objects.published()
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class ManList(ListAPIView):
    queryset=Product.objects.published().filter(gender='male')
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class WomanList(ListAPIView):
    queryset=Product.objects.published().filter(gender='female')
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class BrandProductList(ListAPIView):
    # queryset=Product.objects.published()
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        brand=get_object_or_404(Brand,pk=pk)
        pro=brand.product.all()
        return pro
class Branddetail(RetrieveAPIView):
    # queryset
    serializer_class=BrandSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        brand=Brand.objects.filter(pk=pk)
        return brand
class BrandList(ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class PantsList(ListAPIView):
    queryset=Product.objects.published().filter(type="pants")
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class ShirtList(ListAPIView):
    queryset=Product.objects.published().filter(type="shirt")
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class ShoseList(ListAPIView):
    queryset=Product.objects.published().filter(type="shose")
    serializer_class=ProductSerializer
    # filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=[AllowAny,]
class SpecialDetail(RetrieveAPIView):
    serializer_class=Spechial2Serializer
    permission_classes=[AllowAny,]
    
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Special.objects.filter(pk=pk)
