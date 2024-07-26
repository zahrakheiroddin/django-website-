from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
        .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    image = models.ImageField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day, self.slug])

class DanPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:news_detail',args=[self.id, self.slug])

