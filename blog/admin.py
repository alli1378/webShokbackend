from django.contrib import admin
from .models import Article,Category
# Register your models here.
def make_published(modeladmin,request,queryset):
    row_updated=queryset.update(status='p')
    if row_updated == 1:
        message_bit='منتشر شد'
    else:
        message_bit='منتشر شدند'
    modeladmin.message_user(request,'{} مقاله {}'.format(row_updated,message_bit))
make_published.short_description='مقالاتی را که میخواهید منتشر شود را انتخواب کنید.'
def make_draft(modeladmin,request,queryset):
    row_updated=queryset.update(status='d')
    if row_updated == 1:
        message_bit='پیشنویس شد'
    else:
        message_bit='پیشنویس شدند'
    modeladmin.message_user(request,'{} مقاله {}'.format(row_updated,message_bit))
make_draft.short_description='مقالاتی را که میخواهید پیشنویس شود را انتخواب کنید.'
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','position','parent','slug','status')
    list_filter=(['status'])
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','jpublish','status','category_to_str')
    list_filter=('publish','status','author')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}
    ordering=['status','-publish']
    actions=[make_published, make_draft]
    
admin.site.register(Article,ArticleAdmin)
