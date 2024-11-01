from django.db import models
from django.urls.base import reverse
# from django.contrib.auth.models import User
from django.utils import  timezone
from extentions.utils import jalali_converter
from blog.models import Category
from account.models import User
# Create your models here.

class ProductManager(models.Manager):
    def published(self):
        return self.filter(status='p')
    def shose(self):
        return self.filter(type='shose')
    def pants(self):
        return self.filter(type='pants')
    def shirt(self):
        return self.filter(type='shirt')
    def headgear(self):
        return self.filter(type='headgear')
    def manto(self):
        return self.filter(type='manto')
    # def manto(self):
    #     return self.filter(seller='manto')

# class SpesialManager(models.Manager):
#     def shose(self):
#         return self.product.all()


class Brand(models.Model):
    thumbnail      =models.ImageField(upload_to='images',verbose_name='عکس',default=None)
    title      =models.CharField(max_length=200,verbose_name='نام برند')
    slug       =models.SlugField(unique=True,max_length=200,verbose_name='آدرس برن')
    employe    =models.ManyToManyField(User,related_name='brand',default=None,verbose_name='کارمند')
    description=models.TextField(verbose_name='توضیح')
    def get_absolute_url(self):
        return reverse('account:profile')
    # def employe_to_str(self):
    #     return 'و'.join([employe.email for employe in self.employe.allemp()])
        
class Product(models.Model):
    STATUS_CHOICES=(
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )
    STATUS=(
        ('shose','کفش'),
        ('pants','شلوار'),
        ('shirt','پیراهن'),
        ('headgear','روسری'),
        ('manto','مانتو'),
    )
    CHOICES=(
            ('red','قرمز'),
            ('blue','آبی'),
            ('yellow','زرد'),
            ('green','سبز'),
            ('black','سیاه'),
            ('gray','خاکستری'),
            ('white','سفید'),
            )
    CHOICES_GENDER=(
            ('male','مرد'),
            ('female','زن'),
            ('kid','کودک')
                        )
    category       =models.ManyToManyField(Category,related_name='product',verbose_name='دسته بندی محصول')
    thumbnail      =models.ImageField(upload_to='images',verbose_name='عکس',default=None)
    color          =models.CharField(max_length=10,choices=CHOICES,verbose_name='رنگ',default=None)
    title          =models.CharField(max_length=200,verbose_name='عنوان کالا')
    type           =models.CharField(max_length=10,choices=STATUS,verbose_name='نوع محصول',default=None)
    description    =models.TextField(verbose_name='توضیح')
    slug           =models.SlugField(unique=True,max_length=200,verbose_name='آدرس محصول')
    publish        =models.DateTimeField(default=timezone.now,verbose_name='زمان')
    created        =models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    updated        =models.DateTimeField(auto_now=True,verbose_name='زمان آپدیت')
    status         =models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name='وضعیت')
    brand          =models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='product',verbose_name='برند' ,default=None)
    seller         =models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_seller',verbose_name='فروشنده' ,default=None)
    favourite      =models.ManyToManyField(User,related_name='favourite_product',default=None,blank=True,verbose_name='محصولات مورد علاقه ی شما')
    price          =models.DecimalField(max_digits=10,decimal_places=0,verbose_name='قیمت',default=0)
    gender         =models.CharField(max_length=7,choices=CHOICES_GENDER,verbose_name='جنسیت',default=None)
    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"
        ordering=['-publish']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('account:product-list')
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description='زمان انتشار'
    def category_to_str(self):
        return 'و'.join([category.title for category in self.category.status_true()])
    objects=ProductManager()

class Special(models.Model):
    STATUS_CHOICES=(
        ('m','مدیوم'),
        ('l','لارج'),
        ('xl','ایکس لارج'),
        ('xxl','دو ایکس لارج'),
        ('xxxl','سه ایکس لارج'),
    )
    STATUS=(
        ('32','۳۲'),
        ('33','۳۳'),
        ('34','۳۴'),
        ('35','۳۵'),
        ('36','۳۶'),
        ('37','۳۷'),
        ('38','۳۸'),
        ('39','۳۹'),
        ('40','۴۰'),
        ('41','۴۱'),
        ('42','۴۲'),
        ('43','۴۳'),
        ('44','۴۴'),
        ('45','۴۵'),
        ('46','۴۶'),

    )
    sizepants       =models.CharField(max_length=4,choices=STATUS_CHOICES,verbose_name='سایز',null=True)
    sizeshose       =models.CharField(max_length=4,choices=STATUS,verbose_name='سایز',null=True)
    sizeshirt       =models.CharField(max_length=4,choices=STATUS_CHOICES,verbose_name='سایز',null=True)
    price          =models.DecimalField(max_digits=10,decimal_places=0,verbose_name='قیمت',default=0)
    count      =models.IntegerField(default=0,verbose_name='تعداد')
    seller_2         =models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller_2',verbose_name='فروشنده' ,default=None)
    product    =models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE,blank=True,default=None,verbose_name='محصولات')
    def get_absolute_url(self):
        return reverse('account:product-list')
    class Meta:
        unique_together=('sizepants','sizeshose','sizeshirt','seller_2')