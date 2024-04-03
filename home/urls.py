from django.urls import path,include
from .views import Home,About,Contact

app_name='home'

urlpatterns=[
    path("",Home.as_view(),name="home"),
    path("about/",About.as_view(),name="about"),
    path("contact/",Contact.as_view(),name="contact")
]