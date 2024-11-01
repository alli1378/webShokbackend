from django.db import models
from account.models import User
from django.utils import  timezone
from extentions.utils import jalali_converter
from django.urls.base import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')
class CategoryManager(models.Manager):
    def status_true(self):
        return self.filter(status=True)
# Create your models here.
class Category(models.Model):
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children',verbose_name='زیر دسته')
    title=models.CharField(max_length=200,verbose_name='عنوان دسته بندی')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='آدرس دسته بندی')
    status=models.BooleanField(default=True,verbose_name="آیا ")
    position=models.IntegerField(verbose_name='وضعیت')
    class Meta:
        verbose_name="دسته"
        verbose_name_plural="دسته ها"
        ordering=['parent__id','position']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('account:home')
    objects=CategoryManager()

class Article(models.Model):
    STATUS_CHOICES=(
        ('d','پیش نویس'),       #draft
        ('p','منتشر شده'),      #publish
        ('i','در حال برسی'),    #investigation
        ('b','برگشت داده شده'), #back
    )
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='article',verbose_name='نویسنده')
    category=models.ManyToManyField(Category,verbose_name='دسته بندی',related_name='article')
    favourite=models.ManyToManyField(User,related_name='article_fav',default=None,blank=True)
    title=models.CharField(max_length=200,verbose_name='عوان')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='آدرس')
    description=models.TextField(verbose_name='متن')
    thumbnail=models.ImageField(upload_to='images',verbose_name='عکس',null=True)
    publish=models.DateTimeField(default=timezone.now,verbose_name='زمان')
    created=models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    updated=models.DateTimeField(auto_now=True,verbose_name='زمان آپدیت')
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name='وضعیت')
    comments=GenericRelation(Comment)
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
        ordering=['-publish']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('account:home')
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description='زمان انتشار'
    def category_to_str(self):
        return ' و'.join([category.title for category in self.category.status_true()])
    category_to_str.short_description='دسته بندی ها'


    objects=ArticleManager()
