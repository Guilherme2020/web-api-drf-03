from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Address(models.Model):

    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.OneToOneField(Address,on_delete = models.CASCADE)

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.CharField(max_length=200)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


    def __str__(self):
        return "%s - %s" % (self.email, self.name)