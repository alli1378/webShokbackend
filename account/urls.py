from django.urls import path
from django.contrib.auth import views
from .views import (ArticleCreate
                    ,ArticleList
                    ,CategoryCreate
                    ,ArticleUpdate
                    ,ArticleDelete
                    ,ProductCreate
                    ,Productlist
                    ,ShirtCreate
                    ,ShoseCreate
                    ,PantsCreate
                    ,Profile
                    ,BrandCreate
                    ,BrandList
                    ,MemberList
                    ,MemberUpdate
                    )
app_name='account'

urlpatterns = [

    path('',ArticleList.as_view(),name='home'),
    path('create/',ArticleCreate.as_view(),name='create'),
    path('update-article/<int:pk>',ArticleUpdate.as_view(),name='update-article'),
    path('delete-article/<int:pk>',ArticleDelete.as_view(),name='delete-article'),
    # category
    path('create-cat/',CategoryCreate.as_view(),name='create-cat'),
    # path('update-cat/',CategoryUpdate.as_view(),name='update-cat'),
    # brand
    path('create-brand/',BrandCreate.as_view(),name='brand-create'),
    path('brand-list/',BrandList.as_view(),name='brand-list'),
    # member
    path('member-list/',MemberList.as_view(),name='member_list'),
    path('member-update/<int:pk>',MemberUpdate.as_view(),name='update-member'),
    
    # MemberUpdate
    # product
    path('product-list/',Productlist.as_view(),name='product-list'),
    path('shose-create/',ShoseCreate.as_view(),name='create-shose'),
    path('shirt-create/',ShirtCreate.as_view(),name='create-shirt'),
    path('pants-create/',PantsCreate.as_view(),name='create-pants'),
    path('product-create/',ProductCreate.as_view(),name='create-product'),
    # profile
    path('profile/',Profile.as_view(),name='profile'),

]
