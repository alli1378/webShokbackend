from django.urls import path
from .views import (
                    ArticleList,
                    ArticleDetail,
                    ArticleCategoryList,
                    ArticleAuthorList,
                    FavouriteList,
                    )

app_name='blog_api'
urlpatterns = [
    path('', ArticleList.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(),name='detail'),
    # path('preview/<int:pk>', ArticlePreview.as_view(),name='preview'),
    path('category/<int:pk>', ArticleCategoryList.as_view(),name='category'),
    path('author/<slug:username>', ArticleAuthorList.as_view(),name='author'),
    # path('fav/<int:id>',favourite_add,name='favourite_add'),
    path('favourite/',FavouriteList.as_view(),name='favourite_list'),
    # path('favourite/page/<int:page>',favourite_list,name='favourite_list'),
]