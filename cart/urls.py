from django.urls import path,include,re_path
from .views import detail
from .views import CartAdd
app_name='cart'
urlpatterns = [
    path('',detail,name='detail'),
    path('add/<int:product_id>',CartAdd, name='cart-add')
]
