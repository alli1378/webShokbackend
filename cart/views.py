from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from Product.models import Product
from .forms import CartAddForm
from django.views.decorators.http import require_POST
# Create your views here.
def detail(request):
    cart=Cart(request)
    return render(request,"cart/detail.html")

@require_POST
def CartAdd(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product, id=product_id)
    form =CartAddForm(request.POST)
    if form.is_valid():
        cd=form.changed_data 
        cart.add(product=product,quantity=cd['quantity'])
    return redirect('cart:detail')