import email
from pydoc import describe
from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=100)
    describe=models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    massage= models.TextField()
    
    

    def __str__(self):
        return self.name + "--" + self.username

class Coment(models.Model):
    name = models.CharField(max_length=100)
    massage= models.TextField()

    def __str__(self):
        return self.name +"-"+ self.massage