from django.contrib import admin
from blog.models import Post,Tag,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','author','category']
#要使用admin.site.register注册
#把新增的 PostAdmin 也注册进来
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
