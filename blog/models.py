from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Roboczy'),
        ('publish', 'Publiczny')
    )

    author = models.ForeignKey(User)
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
