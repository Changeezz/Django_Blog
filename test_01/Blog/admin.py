from django.contrib import admin
from Blog.models import Catagory,Tag,Blog,Comment
# Register your models here.

# Register your models here.
class CatagoryAdmin(admin.ModelAdmin):
    list_disapply = ['name']

class TagAdmin(admin.ModelAdmin):
    list_disapply = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_disapply = ['title', 'author', 'content', 'created', 'catagory', 'tags']

class CommentAdmin(admin.ModelAdmin):
    list_disapply = ['blog', 'name', 'email', 'content', 'created']
# 注册模型类
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)