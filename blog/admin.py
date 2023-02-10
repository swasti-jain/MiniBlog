from django.contrib import admin
from .models import Post, Technology,Science,News,ReferenceNo,Contact
# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','category']

@admin.register(Technology)
class TechnologyModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']

@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']

@admin.register(Science)
class TechnologyModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']

@admin.register(ReferenceNo)
class ReferenceModelAdmin(admin.ModelAdmin):
    list_display = ['id','ref']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','message']
