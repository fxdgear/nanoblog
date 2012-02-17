from django.conf.urls.defaults import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('nanoblog.blog.views',
    url(r'^$', 'homepage'),
)
