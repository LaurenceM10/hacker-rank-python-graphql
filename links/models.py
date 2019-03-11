from django.db import models


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)


class Book(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
