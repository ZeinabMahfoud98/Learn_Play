from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name="index.html"

class About(TemplateView):
    template_name="about.html"

class Contact(TemplateView):
    template_name="contact.html"