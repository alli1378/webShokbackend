# from backend.config.blog.views import favourite_add
from rest_framework import routers, serializers
from blog.models import Article,Category
from account_api.serializers import AuthorOrSellerSerializer 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title']
class ArticleSerializer(serializers.ModelSerializer):
    author=AuthorOrSellerSerializer()
    # favourite=AuthorOrSellerSerializer(many=True)
    category=CategorySerializer(many=True)
    class Meta:
        model=Article
        fields='__all__'
class CategoryArticleSerializer(serializers.ModelSerializer):
    article=ArticleSerializer(many=True)
    class Meta:
        model=Category
        fields=['id','title','article']
        # lookup_field for slug
# class CategoryArticleSerializer(serializers.ModelSerializer):
#     passss