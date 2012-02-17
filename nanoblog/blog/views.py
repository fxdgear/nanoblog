from django.views.generic.base import View, TemplateResponseMixin


class HomepageView(View, TemplateResponseMixin):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


homepage = HomepageView.as_view()
