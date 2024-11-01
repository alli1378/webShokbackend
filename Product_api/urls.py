from django.urls import path
from django.contrib.auth import views
from .views import (ProductDetail,
                    ProductList,  
                    BrandProductList,
                    ProductSpecialList,
                    SpecialDetail,
                    PantsList,
                    ManList,
                    WomanList,
                    BrandList,
                    Branddetail,
                    ShirtList,
                    ShoseList
                    )
app_name='product_api'
urlpatterns=[
    path('products',ProductList.as_view(),name='home'),
    path('product/special/<int:pk>',ProductSpecialList.as_view(),name='special-pro'),
    path('special/<int:pk>',SpecialDetail.as_view(),name='special-pro'),
    path('product/<int:pk>',ProductDetail.as_view(),name='pro-detail'),
    path('products/pants',PantsList.as_view(),name='pants'),
    path('products/shose',ShoseList.as_view(),name='shose'),
    path('products/shirt',ShirtList.as_view(),name='shirt'),
    path('products/man',ManList.as_view(),name='man'),
    path('products/woman',WomanList.as_view(),name='woman'),
    path('products/brand/<int:pk>',BrandProductList.as_view(),name='brand-pro'),
    path('brand/<int:pk>',Branddetail.as_view(),name='brand-detail'),
    path('brand/',BrandList.as_view(),name='brand'),
    # path('home/',home,name='homee'),
    # path('product-detail/<slug:slug>',ProductDetail,name='detail'),
    # path('category-product/<slug:slug>',CategoryList.as_view(),name='product_category'),
    # path('category-product/<slug:slug>/page/<int:page>',CategoryList.as_view(),name='product_category'),
    # path('fav/<int:id>',favourite_add,name='favourite_add'),
    # path('favourite',favourite_list.as_view(),name='favourite_product'),
    # path('favourite/page/<int:page>',favourite_list.as_view(),name='favourite_product'),

]
