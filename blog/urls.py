from django.urls import path
from .views import (ArticleList,
                    ArticleDetail,
                    ArticlePreview,
                    CategoryList,
                    AuthorList,
                    favourite_add,
                    favourite_list
                    )

app_name='blog'
urlpatterns = [
    path('', ArticleList.as_view(),name='home'),
    path('page/<int:page>', ArticleList.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(),name='detail'),
    path('preview/<int:pk>', ArticlePreview.as_view(),name='preview'),
    path('category/<slug:slug>', CategoryList.as_view(),name='category'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(),name='category'),
    path('author/<slug:username>', AuthorList.as_view(),name='author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(),name='author'),
    path('fav/<int:id>',favourite_add,name='favourite_add'),
    path('favourite',favourite_list.as_view(),name='favourite_list'),
    path('favourite/page/<int:page>',favourite_list,name='favourite_list'),
]
