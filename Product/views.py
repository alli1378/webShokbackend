from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DeleteView,DetailView,UpdateView
from .models import Brand,Product,Special
from blog.models import Category,Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from cart.forms import CartAddForm
# Create your views here.
# @login_required
def favourite_add(request,id):
    product=get_object_or_404(Product.objects.published(),id=id)
    if product.favourite.filter(id=request.user.id):
        product.favourite.remove(request.user)
    else:
        product.favourite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
class favourite_list(LoginRequiredMixin,ListView):
    template_name='Product/favourite.html'
    paginate_by=2
    def get_queryset(self):
        favourite=self.request.user
        product=Product.objects.filter(favourite=favourite)
        return product

def home(request):
    articles=Article.objects.published().order_by("-publish")[:9]
    context={
        'articles':articles,
    }
    return render(request,'Product/home.html',context)
class ProductList(ListView):
    # model=Article
    # template_name='blog/Home.html'
    context_object_name='products'
    queryset=Product.objects.published()
    paginate_by=2
def ProductDetail(request,slug):
    # Product.filter
    product=get_object_or_404(Product.objects.published(),slug=slug)
    product_like=Product.objects.filter(type=product.type)
    # product_like=Product.objects.raw('select * From Product where type=product.type')

    context={
    'product':product,
    'form':CartAddForm,
    'product_like':product_like
    }

    return render(request,'Product/product_detail.html',context)
# class ProductDetail(DetailView):
#     context_object_name='product'
#     template_name='Product/product_detail.html'
#     form_class=CartAddForm
#     def get_object(self):
#         slug=self.kwargs.get('slug')
#         return get_object_or_404(Product.objects.published(),slug=slug)


class CategoryList(ListView):
    paginate_by=2
    template_name='Product/category-product.html'
    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category= get_object_or_404(Category.objects.status_true(),slug=slug)
        return category.product.published()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=category
        return context


class BrandList(ListView):
    template_name='blog/brand-product.html'
    paginate_by=2
    def get_queryset(self):
        global brand
        slug=self.kwargs.get('slug')
        brand= get_object_or_404(Brand,slug=slug)
        return brand.product.published()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=category
        return context
