from django.db import models

# Create your models here.
class UserProfile(models.Model):
    #user_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    #author_id = models.AutoField(primary_key=True, unique=True, default= 0)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    isbn = models.CharField(max_length=13, null = True, blank = True)
    #author = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    