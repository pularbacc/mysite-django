from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'landing/index.html'

class AboutView(generic.TemplateView):
    template_name = 'landing/about.html'
