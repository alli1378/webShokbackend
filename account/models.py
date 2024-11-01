from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.db.models import Q
# from Product.models import  Brand
# Create your models here.
# class UserManager(models.Manager):
    # def allemp(self):
    #     self.filter(is_seller=True)
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username})|
            Q(**{self.model.EMAIL_FIELD: username})

        )
class User(AbstractUser):
   
    email    =models.EmailField(unique=True ,null=True,verbose_name='ایمیل')
    is_author=models.BooleanField(default=False,verbose_name='وضعیت نویسنده')
    is_seller=models.BooleanField(default=False,verbose_name='وضعیت فروشنده')

    objects=CustomUserManager()