from django.contrib import admin
from .models import Category, Product,Comment,Brand,Adv,special,SpecialItem,opinion
from django.db import models
from django.forms import Textarea
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={
                                  'style': 'direction: rtl;'})},
    }
@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['name','active', 'email', 'body']
    list_filter = ['created','active']
@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    list_display = ['name','created']
class Specialitmeinline (admin.TabularInline):
    model = SpecialItem
    raw_id_fields = ['product']
@admin.register(special)
class specialAdmin (admin.ModelAdmin):
    list_display = ['id', 'subject']
    inlines = [Specialitmeinline]
admin.site.register(opinion)
