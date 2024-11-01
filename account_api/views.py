from django.http.response import Http404
from django.shortcuts import render,get_list_or_404
from django.urls import reverse_lazy
from .serializers import (
                        UserSerializer,
                        ArticleSerializer,
                        CategorySerializer,
                        AuthorOrSellerSerializer,
                        ProductSerializer,
                        ShirtSeializer,
                        ShoseSeializer,
                        ShoseCreateSeializer,
                        PantsSeializer,
                        PantsCreateSeializer,
                        ProductsellerSerializer,
                        ProductcreateSerializer,
                        BrandSerializer,
                        ArticleAuthorSerializer
                        )

from rest_framework.permissions import IsAdminUser,IsAuthenticated 
from .permissions import (
                        IsSuperUser,
                        IsAuthor,
                        IsSpecial,
                        IsStaff,
                        IsSuperUserOrStaffReadOnly,
                        IsAuthorCreate,
                        IsSeller,
                        IsSellerCreate
                        )
from rest_framework.generics import (CreateAPIView
                                    ,RetrieveAPIView
                                    ,ListAPIView
                                    ,RetrieveDestroyAPIView
                                    ,RetrieveUpdateAPIView
                                    )
from rest_framework.views import APIView
from account.models import User
from blog.models import Article,Category
from Product.models import Product, Special ,Brand
from account.mixins import FieldMixin
from .mixins import (
                    ArticleAccessMixin,
                    ProductAccessMixin,
                    PantsAccessMixin,
                    ShoseAccessMixin,
                    ShirtAccessMixin,
                    ProfileMixin
                    )
from django.http.response import Http404 
# Create your views here.
class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filterset_fields=['first_name','last_name','username','is_author','is_seller']
    permission_classes=(IsSuperUserOrStaffReadOnly,)
class UserCreate(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)
class UserUpdate(RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)
class UserDetail(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)
class UserDelete(RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)
'''
    This views for article list ,article delete,article update,article create
'''
class ArticleList(ListAPIView):
    serializer_class=ArticleSerializer
    permission_classes=(IsAuthorCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Article.objects.all()
        # if user.is_author:
        #     return Article.objects.filter(author=user)
        if user.is_anonymous:
            return 

        return Article.objects.filter(author=user)
class ArticleCreate(CreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleAuthorSerializer
    permission_classes=(IsAuthorCreate,)

# class ArticleCreateGet(ArticleAccessMixin,ListAPIView):
#     queryset=Article.objects.all()
    # def get(self,request,format=None):
    #     return Article.objects.all()
    # serializer_class=ArticleSerializer
    # permission_classes=(IsAuthorCreate,)
class AuthorOrSellerMain(ListAPIView):
    queryset=User.objects.all()
    # def get(self,request,format=None):
    #     return Article.objects.all()
    serializer_class=AuthorOrSellerSerializer
    # permission_classes=(IsAuthorCreate,)

class ArticleUpdate(RetrieveUpdateAPIView):
    queryset=Article.objects.all()
    permission_classes=(IsAuthor,)
    serializer_class=ArticleAuthorSerializer

class ArticleDelete(RetrieveDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(IsStaff,)
'''
    This views

'''
class CategoryCreate(CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsSpecial,)
class CategoryUpdate(RetrieveUpdateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsSuperUser,)
class CategoryDelete(RetrieveDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsSuperUser,)
class CategoryList(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsSpecial,)
'''
'''
class ProductList(ListAPIView):
    serializer_class=ProductSerializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Product.objects.all()
        # if user.is_anonymous or user.is_author and not user.is_seller:
        #     return 
        return Product.objects.filter(seller=user)
class ProductUpdate(RetrieveUpdateAPIView):
    # serializer_class=ProductSerializer
    queryset=Product.objects.all()
    serializer_class=ProductcreateSerializer
    # permission_classes=(IsSellerCreate,)
    # def get_queryset(self):
    #     user = self.request.user
    #     # id=user.id
    #     # pk=self.kwargs.get('pk')
    #     if user.is_anonymous==False:
            
    #         if user.is_staff:
    #             return Product.objects.all()
    #         elif user.is_seller:
    #             return Product.objects.filter(seller=user)
    #         else:
    #             return
        
class ProductCreate(CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductcreateSerializer
    permission_classes=(IsSellerCreate,)
class ProductDelete(ProductAccessMixin,RetrieveDestroyAPIView):
    permission_classes=(IsSellerCreate,)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()
        if self.request.user.is_seller:
            return Product.objects.filter(seller=self.request.user)
class SpecialShirt(ListAPIView):
    # queryset=Product.objects.shirt()
    serializer_class=ProductsellerSerializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Product.objects.shirt()
        if user.is_seller:
            return Product.objects.filter(type='shirt',seller=user)
        if user.is_anonymous:
            return 

    # def perform_create(self, serializer):
    #     if not self.request.user.is_staff:
    #         serializer.product=Product.objects.filter(seller=self.request.user)
    #         # serializer.save(author=self.request.user)

    #     return super().perform_create(serializer)
class SpecialPants(ListAPIView):
    # queryset=
    serializer_class=ProductsellerSerializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Product.objects.pants()
        if user.is_seller:
            return Product.objects.filter(type='pants',seller=user)
        if user.is_anonymous:
            return 

    # def perform_create(self, serializer):
    #     if not self.request.user.is_staff:
    #         serializer.product=Product.objects.filter(seller=self.request.user)
    #         # serializer.save(author=self.request.user)

    #     return super().perform_create(serializer)
class SpecialShose(ListAPIView):
    # queryset=Product.objects.shose()
    serializer_class=ProductsellerSerializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Product.objects.shose()
        if user.is_seller:
            return Product.objects.filter(seller=user,type="shose")
        if user.is_anonymous:
            return 
class ShirtCreate(CreateAPIView):
    queryset=Special.objects.all()
    serializer_class=ShirtSeializer
    # permission_classes=(IsSellerCreate,)
class ShoseCreate(CreateAPIView):
    queryset=Special.objects.all()
    serializer_class=ShoseCreateSeializer
    # permission_classes=(IsSellerCreate,)
class PantsCreate(CreateAPIView):
    queryset=Special.objects.all()
    serializer_class=PantsCreateSeializer
    permission_classes=(IsSellerCreate,)
class ShirtUpdate(RetrieveUpdateAPIView):
    # queryset=Special.objects.all()
    serializer_class=ShirtSeializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Special.objects.all()
        if self.request.user.is_seller:
            # pro=Product.objects.filter(seller=self.request.user)
            return Special.objects.filter(seller_2=self.request.user)
            
            # serializer.save(author=self.request.user)

        # return super().perform_create(serializer)
class ShoseUpdate(RetrieveUpdateAPIView):
    # queryset=Special.objects.all()
    serializer_class=ShoseCreateSeializer
    permission_classes=(IsSellerCreate,)
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Special.objects.all()
        if self.request.user.is_seller:
            return Special.objects.filter(seller_2=self.request.user)

            # serializer.save(author=self.request.user)

        # return super().perform_create(serializer)
class PantsUpdate(RetrieveUpdateAPIView):
    # queryset=Special.objects.all()
    serializer_class=PantsCreateSeializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Special.objects.all()
        if self.request.user.is_seller:
            return Special.objects.filter(seller_2=self.request.user)

            # serializer.save(author=self.request.user)

        # return super().perform_create(serializer)
class ShirtList(ListAPIView):
    serializer_class=ShirtSeializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Special.objects.exclude(sizeshirt__exact='')
        # if user.is_anonymous or user.is_author and not user.is_seller:
        #     return 
        if self.request.user.is_seller:
            return Special.objects.filter(seller_2=user).exclude(sizeshirt__exact='')

class ShoseList(ListAPIView):
    serializer_class=ShoseSeializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Special.objects.exclude(sizeshose__exact='')
        # if user.is_anonymous or user.is_author and not user.is_seller:
        #     return 
        if self.request.user.is_seller:
            return Special.objects.filter(seller_2=user).exclude(sizeshose__exact='')
class PantsList(ListAPIView):
    serializer_class=PantsSeializer
    permission_classes=(IsSellerCreate,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Special.objects.exclude(sizepants__exact='')
        # if user.is_anonymous or user.is_author and not user.is_seller:
        #     return 
        if self.request.user.is_seller:
            return Special.objects.filter(seller_2=user).exclude(sizepants__exact='')

class PantsDelete(PantsAccessMixin,RetrieveDestroyAPIView):
    permission_classes=(IsSellerCreate,)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Special.objects.all()
        if self.request.user.is_seller:
            return Special.objects.filter(seller=self.request.user)
class ShirtDelete(ShirtAccessMixin,RetrieveDestroyAPIView):
    permission_classes=(IsSellerCreate,)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Special.objects.all()
        if self.request.user.is_seller:
            return Special.objects.filter(seller=self.request.user)
class ShoseDelete(ShoseAccessMixin,RetrieveDestroyAPIView):
    permission_classes=(IsSellerCreate,)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Special.objects.all()
        if self.request.user.is_seller:
            return Special.objects.filter(seller=self.request.user)
'''
brand
'''
class BrandList(ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    # permission_classes=(IsStaff,)
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff:
    #         return Brand.objects.all()
class BrandCreate(CreateAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    permission_classes=(IsStaff,)

class BrandDelete(RetrieveDestroyAPIView):
    serializer_class=BrandSerializer
    permission_classes=(IsStaff,)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Brand.objects.all()
class BrandUpdate(RetrieveUpdateAPIView):
    serializer_class=BrandSerializer
    queryset=Brand.objects.all()

    # permission_classes=(IsSellerCreate,)
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff:
    #         return Brand.objects.all()
    #     if user.is_seller:
    #         return Brand.objects.filter(employe=user)
'''
Profile
'''
# class Profile(RetrieveAPIView):
class Profile(ProfileMixin,RetrieveUpdateAPIView):
    # model=User
    # form_class=ProfileForm
    # template_name='registration/profile.html'
    permission_classes=(IsAuthenticated,)
    # success_url=reverse_lazy('account_api:profile')
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    # def get_form_kwargs(self):
    #     kwargs=super(Profile,self).get_form_kwargs()
    #     kwargs.update({
    #         'user':self.request.user,
    #     })
    #     return kwargs
        # if user.is_anonymous or user.is_author and not user.is_seller:
        #     return 
        # if self.request.user.is_seller:
        #     return Brand.objects.filter(employe=user)

    # def get_serializer_class(self):
    #     return ShirtSeializer(context={'request': self.request})
    # def get_serializer_kwargs(self):
    #     kwargs = super(ShirtCreate, self).get_serializer_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs
    # def get_context_data(self):
    #     kwargs=super(ShirtCreate,self).get_form_kwargs()
    #     kwargs['user']=self.request.user
    #     return kwargs
    # def put(self, request, *args, **kwargs):
    #         data = request.data.copy()
    #         data['user'] = self.request.user
    #         return data
            # serializer = self.get_serializer(data=data)

    # def perform_create(self, serializer):
    #     if not self.request.user.is_staff:
    #         # serializer.fields['product'].view_set=Product.objects.shirt().filter(seller=self.request.user)
    #         # serializer.get()
    #         serializer.save()
    #     return super().perform_create(serializer)
# cl
    # serializer_class.fields['product'].queryset=Product.objects.shirt().filter(seller=self.request.user)

    # def put(self):
    #         data=super(ShirtCreate,self).get_form_kwargs()
    #         data['user']=self.request.user
    #         return data    
    # def get(self,request):
    #     data=self.get_object()
    #     data.product=Product.objects.shirt().filter(seller=request.user)
    #     return data

