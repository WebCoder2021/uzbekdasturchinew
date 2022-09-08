import re
from venv import create
from django.db import models
from ckeditor.fields import RichTextField

from users.models import CustomUser

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    def count_posts(self):
        return Post.objects.filter(category=self).count()


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
class PostTags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(PostCategory,on_delete=models.CASCADE, verbose_name="Kategoriyasi")
    tags = models.ManyToManyField(PostTags, verbose_name="Taglar")
    image = models.ImageField(upload_to='maqolalar/', verbose_name="Rasmi")
    title = models.CharField(max_length=200, verbose_name="Sarlavhasi")
    sub_title =  models.CharField(max_length=400, verbose_name="Qisqa mazmuni", blank=True, null=True)
    content = RichTextField(verbose_name="Mazmuni", blank=True, null=True)
    views = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, verbose_name="Slug")
    publish = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, default=1)
    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
    def __str__(self):
        return self.title
    def likes(self):
        if PostLike.objects.filter(post__title=self.title).exists():
            like = PostLike.objects.filter(post__title=self.title).first()
            return like.users
        else: return 0
    def dislikes(self):
        if PostDisLike.objects.filter(post__title=self.title).exists():
            dislike = PostDisLike.objects.filter(post__title=self.title).first()
            return dislike.users
        else: return 0
    def comments(self):
        comment = Comment.objects.filter(post__title=self.title).all()
        return comment
class PostLike(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE,unique=True)
    users = models.ManyToManyField(CustomUser)
    class Meta:
        verbose_name = 'Maqola like'
        verbose_name_plural = 'Maqola likelar'
    def __str__(self):
        return self.post.title
class PostDisLike(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE,unique=True)
    users = models.ManyToManyField(CustomUser)
    class Meta:
        verbose_name = 'Maqola dislike'
        verbose_name_plural = 'Maqola dislikelar'
    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content
    class Meta:
        verbose_name = 'Maqola kommentariya'
        verbose_name_plural = 'Maqola kommentariyalari'