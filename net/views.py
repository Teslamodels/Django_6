from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Info(TemplateView):
    template_name = 'index.html'

class math(TemplateView):
    template_name = 'net.html'