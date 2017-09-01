from django.test import TestCase
from blog.templatetags import blog_tags
from blog.models import Post,Tag,Category

# Create your tests here.
class MyTest(TestCase):
    def testBlogTag(self):
        print('get_recent_posts----')
        posts = blog_tags.get_recent_posts()
        print(posts)
        print(Post.objects.all())
        print('categories----')
        categories  = blog_tags.get_categories()
        print(categories)
        print('get_tags----')
        tags = blog_tags.get_tags()
        print(tags)


        print('archives----')
        archives = blog_tags.archives()
        print(archives)