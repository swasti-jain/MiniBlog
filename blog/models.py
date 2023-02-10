from django.db import models

# Create your models here.
POST_CHOICES = (
    ('general','GENERAL'),
    ('technology','TECHNOLOGY'),
    ('science', 'SCIENCE'),
    ('news','NEWS'),
   
)

# class MyModel(models.Model):
#   color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')


class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    category = models.CharField(max_length=20, choices=POST_CHOICES, default='general')

    
class News(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField() 

class Technology(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()

class Science(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()

class ReferenceNo(models.Model):
    ref = models.CharField(max_length=50)

# class Contact(models.Model):
#     name = models.Char
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    address = models.CharField(max_length=150)
    message = models.TextField()