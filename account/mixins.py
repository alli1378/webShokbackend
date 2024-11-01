from django.http import Http404
from django.shortcuts  import render,get_object_or_404,redirect
from blog.models import Article
class FieldMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            self.fields=('author','title','category','slug','description','thumbnail','status','publish')
        elif request.user.is_author:
            self.fields=('title','category','slug','description','thumbnail','publish')

        else:
            raise Http404
        return super().dispatch(request,*args,**kwargs)
class FieldProductMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            self.fields=('category','thumbnail','title','description','slug','price','publish','type','status','brand','seller','color')
        elif request.user.is_seller:
            self.fields=('category','thumbnail','title','description','slug','price','publish','type','status','brand','color')
        else:
            raise Http404
        return super().dispatch(request,*args,**kwargs)
class FormValidProductMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj=form.save(commit=False)
            self.obj.seller=self.request.user
            self.obj.status='d'

        return super().form_valid(form)

class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj=form.save(commit=False)
            self.obj.author=self.request.user
            self.obj.status='d'

        return super().form_valid(form)
class ArticleUpdateAccessMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        article=get_object_or_404(Article,pk=pk)
        if article.author ==request.user and article.status in ['b','d'] or\
            request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404
class AuthorAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_author or request.user.is_superuser:
                return super().dispatch(request,args,kwargs)
            else:
                return redirect('account:profile')
        else:
            return redirect('login')
class SellerAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_seller:
                return super().dispatch(request,args,kwargs)
            else:
                return redirect('account:profile')
        else:
            return redirect('login')
class SuperUserMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404
