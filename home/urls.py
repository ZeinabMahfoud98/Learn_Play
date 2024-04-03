from django.urls import path,include
from .views import Home,About,Contact,Program,Gallery

app_name='home'

urlpatterns=[
    path("",Home.as_view(),name="home"),
    path("about/",About.as_view(),name="about"),
    path("contact/",Contact.as_view(),name="contact"),
    path("program/",Program.as_view(),name="programs"),
    path("gallery/",Gallery.as_view(),name="gallery")
]