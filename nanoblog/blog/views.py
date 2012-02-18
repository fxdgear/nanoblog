from django.views.generic.base import View, TemplateResponseMixin
from django.http import Http404
from nanoblog.blog.models import Blog


class HomepageView(View, TemplateResponseMixin):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            blog = Blog.objects.get(author=user)
        except:
            raise Http404
        return self.render_to_response({'blog': blog})


homepage = HomepageView.as_view()
