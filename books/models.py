from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=250)
    # one to many relationship
    # book has one category, category has many books, like a library
    category = models.ForeignKey('Category', related_name='books', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(null=False, unique=True)

    def get_asolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Favorite(models.Model):
    book = models.ForeignKey('Book', related_name='favorites', on_delete = models.CASCADE)
    user = models.ForeignKey('User', related_name='favorites', on_delete = models.CASCADE)



    


