from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    image =models.ImageField (upload_to='products',blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug, 'car'])
class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/brand/',blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
    def __str__(self):
        return self.name
    def get_absolute_url(self):

        return reverse('shop:product_list_by_category',args=[self.slug, 'brand'])
class Product(models.Model):

    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    codenum = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    baseprice=models.IntegerField()
    discount=models.IntegerField()
    price = models.IntegerField(default = 0)
    wholesale_price =models.IntegerField(default = 0)
    number =models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if self.discount == 0 or self.discount > 100:
            self.price = self.baseprice

            super(Product, self).save(*args, **kwargs)
        else:
            x=100- self.discount
            y = x * self.baseprice
            self.price = y / 100

            '''if self.speed_score is None:
                self.speed_score = ...

                self.calculate_speed_score()'''

            # Now we call the actual save method
            super(Product, self).save(*args, **kwargs)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id, self.slug])
class Comment(models.Model):
    post = models.ForeignKey(Product,
                            on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
class opinion (models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField()
    def __str__(self):
        return self.title

class Adv (models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/Adv/')
    URLL = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class special(models.Model):
    subject = models.CharField(max_length=50)
    key = models.CharField(max_length=5)

class SpecialItem(models.Model):
    special = models.ForeignKey(special,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='special_items',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
