from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='博客分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'


class Tags(models.Model):
    name = models.CharField(max_length=128, verbose_name='博客标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = '博客标签'


class Entry(models.Model):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    author = models.ForeignKey(User, verbose_name='博客作者',on_delete=models.CASCADE)
    # 此处采用外键
    # User 是这里的 from django.contrib.auth.models import User

    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='博客配图')
    # null=True 表示这个字段在数据库中可以为空，可以没有内容
    # blank=True 表示在admin，就是django的admin的后台创建可以为空。
    # null=True，blank=True 配套出现

    body = models.TextField(verbose_name='博客正文')
    abstract = models.TextField(max_length=256, null=True, blank=True, verbose_name='摘要')
    # 有些人不喜欢用摘要，所以要允许他为空
    visiting = models.PositiveIntegerField(default=0, verbose_name='访问量')

    category = models.ManyToManyField('Category', verbose_name='博客分类')
    # 一个分类下有很多博客，同时博客可以属于不同的分类。这就是多对多

    tags = models.ManyToManyField('Tags', verbose_name='博客标签')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # auto_now_add=True 自动保存博客创建的时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    # auto_now=True 自动把当前时间添加给他

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # 这个方法会自动生成每一篇博客的链接
        return reverse('blog:blog_detail', kwargs={'blog_id': self.id})
        # reverse 会帮我们自动生成url地址
        # 会生成一个id http://127.0.0.1:8000/blog/2  其中的2就是通过self.id获取

    def increase_visiting(self):  # 如何增加浏览量
        self.visiting += 1
        self.save(update_fields=['visiting'])  # 保存到这个字段

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客'
        verbose_name_plural = '博客'
