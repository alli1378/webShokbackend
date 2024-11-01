from django.forms.models import fields_for_model
from django.http import request
from rest_framework import routers, serializers
from account.models import User
from blog.models import Article, Category
from account.mixins import FieldMixin
from Product.models import Product,Brand,Special
from djoser.serializers import UserCreateSerializer
class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=['id','email','last_name','is_author','is_seller','username','password','first_name','is_superuser']
        # lookup_field for slug

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        # lookup_field for slug
class AuthorOrSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','first_name','last_name']
        # lookup_field for slug

class ArticleSerializer(serializers.ModelSerializer):
    author=AuthorOrSellerSerializer()
    class Meta:
        model=Article
        fields='__all__'
        # lookup_field for slug
    # def __init__(self, *args, **kwargs):
    #     super(ArticleSerializer, self).__init__(*args, **kwargs)
class ArticleAuthorSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField()

    # def get_age(self,request,obj):
    #    return getattr(obj, 'author', request.user)

    class Meta:
        model=Article
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
class ProductSerializer(serializers.ModelSerializer):
    seller=AuthorOrSellerSerializer()
    class Meta:
        model=Product
        fields='__all__'
class ProductcreateSerializer(serializers.ModelSerializer):
    # seller=AuthorOrSellerSerializer()
    class Meta:
        model=Product
        fields='__all__'
class ProductsellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('category','title','slug','description','thumbnail','publish','created','updated','id')
class Product2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id',)

class ShirtSeializer(serializers.ModelSerializer):
    # seller_2=AuthorOrSellerSerializer()
    # product=Product2Serializer(read_only=True )
    # def __init__(self,*args,**kwargs):
    #     super(ShirtSeializer,self).__init__(*args,**kwargs)
    #     self.fields['product'].queryset=Product.objects.shirt()        
    class Meta:
        model=Special
        fields=['count','sizeshirt','product','seller_2'
         ,"price",'id'
        ]

class ShoseSeializer(serializers.ModelSerializer):
    seller_2=AuthorOrSellerSerializer()
    product=Product2Serializer()

    def __init__(self,*args,**kwargs):
        super(ShoseSeializer,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.shose()

    class Meta:
        model=Special
        fields=['count','sizeshose','product','seller_2','id','price']

class ShoseCreateSeializer(serializers.ModelSerializer):
    # seller_2=AuthorOrSellerSerializer()
    # product=Product2Serializer()

    # def __init__(self,*args,**kwargs):
    #     super(ShoseSeializer,self).__init__(*args,**kwargs)
    #     self.fields['product'].queryset=Product.objects.shose()

    class Meta:
        model=Special
        fields=['count','sizeshose','product','seller_2'
         ,"price",'id'
        ]

class PantsSeializer(serializers.ModelSerializer):
    seller_2=AuthorOrSellerSerializer()
    product=Product2Serializer()

    def __init__(self,*args,**kwargs):
        super(PantsSeializer,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.pants()

    class Meta:
        model=Special
        fields=['count','sizepants','product','seller_2','id','price'
        ]

class PantsCreateSeializer(serializers.ModelSerializer):
    
    class Meta:
        model=Special
        fields=['count','sizepants','product','seller_2'
         ,"price"
        ]

class ShirtSellerSeializer(serializers.ModelSerializer):
    # current_user = serializers.SerializerMethodField('_user')
    # seller=AuthorOrSellerSerializer()

    # Use this method for the custom field
    # product=ProductsellerSerializer()

    def _user(self):
        request = self.context.get('request', None)
        if request:
            user=request.user.id
            return user

    def __init__(self,*args,**kwargs):
        super(ShirtSellerSeializer,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.shirt().filter(seller=self._user())

    class Meta:
        model=Special
        fields=['count','sizeshirt','product']

class ShoseSellerSeializer(serializers.ModelSerializer):
    def _user(self):
        request = self.context.get('request', None)
        if request:
            user=request.user.id
            return user
    
    def __init__(self,*args,**kwargs):
        super(ShoseSellerSeializer,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.shose().filter(seller=self._user())

    class Meta:
        model=Special
        fields=['count','sizeshose','product'
        ,"price"
        ]

class PantsSellerSeializer(serializers.ModelSerializer):
    def _user(self):
        request = self.context.get('request', None)
        if request:
            user=request.user.id
            return user
    
    def __init__(self,*args,**kwargs):
        super(PantsSellerSeializer,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.pants().filter(seller=self._user())

    class Meta:
        model=Special
        fields=['count','sizepants','product']

'''
Brand
''' 
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
'''
Profile
'''
class ProfileStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name']
