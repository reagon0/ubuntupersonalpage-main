from django.db import models 
from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Author(models.Model):
    name = models.CharField(max_length=100)
    born = models.IntegerField(null=True, blank=True)
    death = models.IntegerField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
          return f'/author/{self.id}/' #('author-detail', args=[str(self.id)])

class Book(models.Model):
    title = models.CharField(max_length=255)
    # Foreign Key used because book can only have one author, but authors can have multiple books    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    date_published = models.IntegerField(null=True, blank=True)
    date_read = models.IntegerField(null=True, blank=True)
    summary = models.TextField(max_length=5000, help_text="Enter a brief description of the book", blank=True)
    my_thoughts = models.TextField(max_length=10000, blank=True, default="")
    coverimage = models.ImageField(null=True, upload_to='images', blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
        null=True,
        blank=True,
    )


