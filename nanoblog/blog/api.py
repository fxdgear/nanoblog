from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization
from nanoblog.blog.models import Blog, Post


class BlogResource(ModelResource):
    class Meta:
        queryset = Blog.objects.all()
        resource_name = 'blog'
        authorization = Authorization()
        filtering = {
            'id': ALL,
            'name': ALL,
            'slug': ALL
        }


class PostResource(ModelResource):
    business = fields.ForeignKey(BlogResource, 'blog')

    class Meta:
        queryset = Post.objects.all()
        authorization = Authorization()
        resource_name = 'post'
        filtering = {
            'id': ALL,
            'created_on': ALL,
            'body': ALL,
            'blog': ALL_WITH_RELATIONS,
        }
