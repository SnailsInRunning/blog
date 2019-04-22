from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):#定制过滤所有的发布过的对象
    def get_queryset(self):#返回执行过的查询集的方法
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250,
                    unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                        related_name="blog_posts")
    body = models.TextField()
    publish= models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now =True)
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    status = models.CharField(max_length=10,
                             choices = STATUS_CHOICES,
                            default = 'draft'
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)
        db_table = 'MyBlog'
    def __str__(self):
        return self.title

    def get_absolute_url(self): #返回对象的标准的URL，通过名字和可选参数构建
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug
                            ]
                       )
        # return reverse('blog:post_detail',args=[1,2])