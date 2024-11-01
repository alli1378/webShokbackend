from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from account.models import User
from django.views.generic import ListView,DetailView,UpdateView
from account.mixins import ArticleUpdateAccessMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article,Category
# Create your views here.
@login_required
def favourite_add(request,id):
    article=get_object_or_404(Article.objects.published(),id=id)
    if article.favourite.filter(id=request.user.id).exists():
        article.favourite.remove(request.user)
    else:
        article.favourite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class favourite_list(LoginRequiredMixin,ListView):
    paginate_by=3
    template_name='blog/favourite.html'
    def get_queryset(self):
        favourite=self.request.user
        article=Article.objects.filter(favourite=favourite)
        return article
class ArticleList(ListView):
    # model=Article
    # template_name='blog/Home.html'
    context_object_name='articles'
    queryset=Article.objects.published()
    paginate_by=2


# def Home(request,page=1):
#   articels_list=Article.objects.published()
#   paginator=Paginator(articels_list,2)
#   articels=paginator.get_page(page)
#   context={
#     'articles':articels
#   }
#   return render(request,'blog/Home.html',context)
class ArticleDetail(DetailView):
    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Article.objects.published(),pk=pk)
class ArticlePreview(ArticleUpdateAccessMixin,DetailView):
    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Article,pk=pk)
class CategoryList(ListView):
    template_name='blog/category.html'
    paginate_by=2
    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category= get_object_or_404(Category.objects.status_true(),slug=slug)
        return category.article.published()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=category
        return context
class AuthorList(ListView):
    template_name='blog/author_list.html'
    paginate_by=2
    def get_queryset(self):
        global author
        username=self.kwargs.get('username')
        author= get_object_or_404(User,username=username)
        return author.article.published()
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['author']=author
    #     return context
# comment
