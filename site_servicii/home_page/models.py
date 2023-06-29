from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title} -> {self.author} -> created on {self.created_on} -> {self.content} -> updated on {self.updated_on} -> {self.status} -> link: {self.slug}"


class Contact(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.email}->{self.date}->{self.subject} -> {self.message}'

# class Localitate:
#     def __init__(self, judet, apartenenta,localitate, id_apartenenta, bcpi):
#         self.judet = judet
#         self.apartenenta = apartenenta
#         self.localitate = localitate
#         self.id_apartenenta = id_apartenenta
#         self.bcpi = bcpi
#
#     def print_localitate(self):
#         print(f'Denumire localitate: {self.localitate}')
#
#     def __str__(self):
#         return f"{self.localitate}"
