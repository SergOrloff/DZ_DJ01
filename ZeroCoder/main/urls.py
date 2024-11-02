from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('data/', views.new, name='page2'),
    path('test/', views.beast, name='page3'),
    path('contacts/', views.contact, name='page4'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)