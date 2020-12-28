from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from .import views


from.import views

urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('contact',views.contact, name= 'contact'),
    path('search',views.search, name= 'search'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)