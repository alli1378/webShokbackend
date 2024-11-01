# from backend.config.account.models import User
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404, render
from blog.models import Article, Category
from .serializers import ArticleSerializer,CategoryArticleSerializer
# from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated  
from account.models import User
# Create your views here.
class ArticleList(ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[AllowAny,]
    
class ArticleDetail(RetrieveAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
class ArticleCategoryList(ListAPIView):
    serializer_class=ArticleSerializer
    permission_classes=[AllowAny,]
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        category=get_object_or_404(Category.objects.status_true(),pk=pk)
        return category.article.published()
class ArticleAuthorList(ListAPIView):
    serializer_class=ArticleSerializer
    permission_classes=[AllowAny,]
    def get_queryset(self):
        username=self.kwargs.get('username')
        author=get_object_or_404(User,username=username)
        return author.article.published()
class FavouriteList(ListAPIView):
    serializer_class=ArticleSerializer
    permission_classes=[IsAuthenticated,]
    def get_queryset(self):
        favourite=self.request.user
        article=Article.objects.filter(favourite=favourite)
        return article