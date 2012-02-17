from django.contrib import admin

from nanoblog.blog.models import *

admin.site.register(Blog)
admin.site.register(Post)
