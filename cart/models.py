from django.db import models
from account.models import User
from Product.models import Special
# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,related_name='orders',verbose_name='مشتری',on_delete=models.CASCADE)
    address= models.CharField(max_length=150,verbose_name='آدرس')
    created=models.DateTimeField(auto_now_add=True)
    paid_amount=models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    class Meta:
        ordering=['-created',]
    # def __str__(self) :
    #     return self.
class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Special,related_name='items',on_delete=models.CASCADE)
    # price=models.DecimalField(max_digits=8,decimal_places=2)
    quntity=models.IntegerField(default=1)
