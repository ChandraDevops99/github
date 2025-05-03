

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

