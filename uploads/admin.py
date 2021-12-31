from django.contrib import admin
from django.db import models
from django.db.models import fields
from .models import Author,Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name','title','birth_date','avatar')
    list_display = ('name','title','birth_date','avatar')
    list_filter = ('birth_date','title')
    search_fields = ('name',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book)