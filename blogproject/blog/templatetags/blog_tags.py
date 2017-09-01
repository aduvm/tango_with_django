from ..models import Post, Tag, Category
from django import template

register = template.Library()  # 为了使标签库有效必须包含 register  变量

# 获取前5篇文章
@register.simple_tag
def get_recent_posts(num=5):
    posts = Post.objects.all()[:]
    print('ss %d'.format(len(posts)))
    return posts





# 获取分类
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()


# 获取本月的而文章
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 获取标签
@register.simple_tag
def get_tags():
    return Tag.objects.all()
