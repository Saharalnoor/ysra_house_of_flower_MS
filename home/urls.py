from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('success/', views.contact_thankyou, name='contact_thankyou')
]