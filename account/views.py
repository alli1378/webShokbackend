from django.http.response import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (FieldMixin,
                    FormValidMixin,
                    ArticleUpdateAccessMixin,
                    SuperUserMixin,
                    AuthorAccessMixin,
                    FormValidProductMixin,
                    FieldProductMixin,
                    SellerAccessMixin,
                    )
from django.views.generic import (ListView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView)
from .forms import (
                    ProfileForm,
                    ShirtForm,
                    ShoseForm,
                    PantsForm
                    )
from .models import User
from blog.models import Article,Category
from Product.models import Brand, Product,Special
# Create your views here.
class ArticleList(AuthorAccessMixin,ListView):
    context_object_name='articles'
    template_name='registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
class ArticleCreate(AuthorAccessMixin,FieldMixin,FormValidMixin,CreateView):
    model=Article
    template_name='registration/article-create-update.html'
    
class ArticleUpdate(ArticleUpdateAccessMixin,FieldMixin,FormValidMixin,UpdateView):
    model=Article
    template_name='registration/article-create-update.html'
class ArticleDelete(SuperUserMixin,DeleteView):
    model=Article
    template_name='registration/article_confirm_delete.html'
    success_url=reverse_lazy('account:home')
# auth

class Login(LoginView):
    def get_success_url(self):
        user=self.request.user
        if user.is_superuser or user.is_seller:
            return reverse_lazy('account:product-list')
        elif user.is_author:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')
class Profile(LoginRequiredMixin,UpdateView):
    model=User
    form_class=ProfileForm
    template_name='registration/profile.html'
    success_url=reverse_lazy('account:profile')
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user,
        })
        return kwargs
class CategoryCreate(LoginRequiredMixin,CreateView):
    model=Category
    fields=['title','slug','position','status','parent']
    template_name='registration/catgory-create-update.html'
# member
class MemberList(LoginRequiredMixin,ListView):
    context_object_name='members'
    template_name='registration/member-list.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
           return User.objects.all() 
        else:
            raise Http404
class MemberUpdate(SuperUserMixin,UpdateView):
    model=User
    template_name='registration/member-profile-update.html'
    fields=['username','email','first_name','last_name','is_author','is_seller']

# Brand
class BrandList(SuperUserMixin,ListView):
    context_object_name='brands'
    template_name='registration/brand.html'
    def get_queryset(self):
        return Brand.objects.all()
class BrandCreate(SuperUserMixin,CreateView):
    model=Brand
    template_name='registration/brand-create-update.html'
    fields=['description','title','employe','slug']
# class BrandUpdate(SuperUserMixin,UpdateView):
#     model=Brand
#     template_name='registration/brand-create-update.html'
#     fields=['description','title','employe','slug']

# productlist
class Productlist(SellerAccessMixin,ListView):
    context_object_name='products'
    template_name='registration/produc.html'
    def get_queryset(self):
        # return Product.objects.all()

        if self.request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.filter(seller=self.request.user)
# productcreate
class ProductCreate(SellerAccessMixin,FieldProductMixin,FormValidProductMixin,CreateView):
    model=Product
    template_name='registration/Product-create.html'
class ShirtCreate(SellerAccessMixin,FormValidProductMixin,CreateView):

    form_class=ShirtForm
    template_name='registration/shirt-create.html'
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(ShirtCreate,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class PantsCreate(SellerAccessMixin,FormValidProductMixin,CreateView):

    form_class=PantsForm
    template_name='registration/pants-create.html'
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(PantsCreate,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class ShoseCreate(SellerAccessMixin,FormValidProductMixin,CreateView):

    form_class=ShoseForm
    template_name='registration/shose-create.html'
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(ShoseCreate,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs





from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class Register(CreateView):
    form_class=SignupForm
    template_name='registration/register.html'
    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی به ایمیل شما ارسال شد<a href="/login">ورود</a>')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        # context={
        #         'uidb64':uidb64,
        #         'token':token,
        #         }
        return HttpResponse('اکانت شما با موفقیت فعال شد برای ورود کلیک کنید<a href="/login">کلیک</a>کنید.')
    else:
        user.delete()
        return HttpResponse('لینک فعال سازی منقضی شده است <a href="/register">دوباره تلاش کنید.</a>')

# def activate(request, uidb64, token):
    # try:
        # uid = force_text(urlsafe_base64_decode(uidb64))
        # user = User.objects.get(pk=uid)
    # except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        # user = None
    # if user is not None and account_activation_token.check_token(user, token):
        # user.is_active = True
        # user.save()
        # login(request, user)
        # return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    # else:
        # return HttpResponse('Activation link is invalid!')


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string('registration/activate_account.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'registration/register.html', {'form': form})
