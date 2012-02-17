import datetime
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u"%s" % self.name


class Post(models.Model):
    created_on = models.DateTimeField(default=datetime.datetime.now)
    body = models.TextField()
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return u"%s" % self.body
