from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from program.models import Program
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.

class Home(TemplateView):
    template_name="index.html"

class About(TemplateView):
    template_name="about.html"


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:contact')  
        else:
            return render(request, self.template_name, {'form': form})

class Gallery(TemplateView):
    template_name="gallery.html"

class ProgramView(TemplateView):
    template_name="programs.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        programs = Program.objects.all()
        context['programs'] = programs
        return context
