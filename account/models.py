from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250,blank=True)
    postal_code = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=20, default= '0')
    city = models.CharField(max_length=100,blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    check = models.BooleanField(default=False)
    def __str__(self):
        return f'Profile for user {self.user.username}'


class wholesale_pass (models.Model):
    wpass = models.CharField(max_length=50)
