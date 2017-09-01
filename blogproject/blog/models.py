from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
#文章
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=100)
    #创建时间
    create_time = models.DateTimeField()
    #修改时间
    modified_time = models.DateTimeField()
    #文章摘要 可以为空
    excerpt = models.CharField(max_length=200,blank = True)
    #文章对应的分类
    category = models.ForeignKey(Category)
    #文章对应的tag 可以为空
    tag = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)

    body = models.TextField(default='')

    def __str__(self):
        return self.title





