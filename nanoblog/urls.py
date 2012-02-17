from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api

from nanoblog.blog.api import BlogResource, PostResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(BlogResource())
v1_api.register(PostResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('nanoblog.blog.urls')),
    url(r'^api/', include(v1_api.urls)),

)
