from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =  128,unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category) #种类
    title = models.CharField(max_length = 128)#标题
    url = models.URLField() #
    views = models.IntegerField(default=0)#访问数量
    def __str__(self):
        return self.title

#增加User的属性
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    def __str__(self):
        return self.user.username