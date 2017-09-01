from django.contrib import admin
from tango.models import Category,Page,UserProfile
from django.db import models
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','views','likes']

class PageAdmin(admin.ModelAdmin):
    list_display = ['title','url','category','views']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)