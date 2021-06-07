from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    decs = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + '|' + str(self.user)

#class Author(models.Model):
 #   user = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
  #  def __str__(self):
   #     return self.name

    #def get_absolute_url(self):
     #   return reverse('author-detail', kwargs={'pk': self.pk})



class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()

    