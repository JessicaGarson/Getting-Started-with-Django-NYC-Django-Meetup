from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
