from django.urls import path,include
from .views import Home,About,ContactView,ProgramView,Gallery

app_name='home'

urlpatterns=[
    path("",Home.as_view(),name="home"),
    path("about/",About.as_view(),name="about"),
    path("contact/",ContactView.as_view(),name="contact"),
    path("program/",ProgramView.as_view(),name="programs"),
    path("gallery/",Gallery.as_view(),name="gallery")
]