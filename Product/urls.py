from django.urls import path
from django.contrib.auth import views
from .views import (BrandList,
                    CategoryList,
                    ProductList,
                    ProductDetail,
                    favourite_add,
                    favourite_list,
                    home,
                    )
app_name='product'
urlpatterns=[
    path('',ProductList.as_view(),name='home'),
    path('home/',home,name='homee'),
    path('product-detail/<slug:slug>',ProductDetail,name='detail'),
    path('category-product/<slug:slug>',CategoryList.as_view(),name='product_category'),
    path('category-product/<slug:slug>/page/<int:page>',CategoryList.as_view(),name='product_category'),
    path('fav/<int:id>',favourite_add,name='favourite_add'),
    path('favourite',favourite_list.as_view(),name='favourite_product'),
    path('favourite/page/<int:page>',favourite_list.as_view(),name='favourite_product'),

]
