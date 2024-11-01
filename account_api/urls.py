from django.urls import path
from .views import (
                    AuthorOrSellerMain,
                    UserCreate,
                    UserDetail,
                    UserList,
                    UserDelete,
                    UserUpdate,
                    ArticleCreate,
                    # ArticleCreateGet,
                    ArticleList,
                    ArticleUpdate,
                    ArticleDelete,
                    CategoryCreate,
                    CategoryDelete,
                    CategoryUpdate,
                    CategoryList,
                    ProductList,
                    ProductCreate,
                    ProductUpdate,
                    ProductDelete,
                    ShirtCreate,
                    ShoseCreate,
                    PantsCreate,
                    ShirtUpdate,
                    ShoseUpdate,
                    PantsUpdate,
                    ShirtList,
                    ShoseList,
                    PantsList,
                    ShirtDelete,
                    ShoseDelete,
                    PantsDelete,
                    BrandList,
                    BrandDelete,
                    BrandUpdate,
                    BrandCreate,
                    SpecialShirt,
                    SpecialPants,
                    SpecialShose,
                    Profile                   
                    )

app_name='account_api'
urlpatterns = [

    path('AuthorOrSeller-main/',AuthorOrSellerMain.as_view(),name='create'),
    # main
    path('article-list/',ArticleList.as_view(),name='home'),
    path('article-create/',ArticleCreate.as_view(),name='create'),
    path('article-update/<int:pk>',ArticleUpdate.as_view(),name='update-article'),
    path('delete-article/<int:pk>',ArticleDelete.as_view(),name='delete-article'),
    # # category
    path('category-list/',CategoryList.as_view(),name='home'),
    path('create-cat/',CategoryCreate.as_view(),name='create-cat'),
    path('update-category/<int:pk>',CategoryUpdate.as_view(),name='update-category'),
    path('delete-category/<int:pk>',CategoryDelete.as_view(),name='delete-category'),
    # # brand
    path('create-brand/',BrandCreate.as_view(),name='brand-create'),
    path('brand-list/',BrandList.as_view(),name='brand-list'),
    path('brand-delete/<int:pk>',BrandDelete.as_view(),name='brand-delete'),
    path('brand-update/<int:pk>',BrandUpdate.as_view(),name='brand-update'),
    # # member
    path('user-list/',UserList.as_view(),name='user-list'),
    path('user-create/',UserCreate.as_view(),name='user-member'),
    path('user-update/<int:pk>',UserUpdate.as_view(),name='user-member'),
    path('user-delete/<int:pk>',UserDelete.as_view(),name='user-member'),
    path('user/<int:pk>',UserDetail.as_view(),name='profile'),
    # # product
    path('product-list/',ProductList.as_view(),name='product-list'),
    path('product-create/',ProductCreate.as_view(),name='create-product'),
    path('product-update/<int:pk>',ProductUpdate.as_view(),name='update-product'),
    path('product-delete/<int:pk>',ProductDelete.as_view(),name='delete-product'),
    # shose
    path('special-shose/',SpecialShose.as_view(),name='create-shose'),
    path('shose-create/',ShoseCreate.as_view(),name='create-shose'),
    path('shose-update/<int:pk>',ShoseUpdate.as_view(),name='update-shose'),
    path('shose-list/',ShoseList.as_view(),name='shose-list'),
    path('delete-shose/<int:pk>',ShoseDelete.as_view(),name='delete-shose'),
    # shirt
    path('special-shirt/',SpecialShirt.as_view(),name='create-shirt'),
    path('shirt-create/',ShirtCreate.as_view(),name='create-shirt'),
    path('shirt-update/<int:pk>',ShirtUpdate.as_view(),name='update-shirt'),
    path('shirt-list/',ShirtList.as_view(),name='shirt-list'),
    path('delete-shirt/<int:pk>',ShirtDelete.as_view(),name='delete-shirt'),
    # pants
    path('special-pants/',SpecialPants.as_view(),name='create-pants'),
    path('pants-create/',PantsCreate.as_view(),name='create-pants'),
    path('pants-list/',PantsList.as_view(),name='pants-list'),
    path('pants-update/<int:pk>',PantsUpdate.as_view(),name='update-pants'),
    path('delete-pants/<int:pk>',PantsDelete.as_view(),name='delete-pants'),

    # # profile
    path('profile/',Profile.as_view(),name='brand-detail'),

]
