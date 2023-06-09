from django.contrib import admin
from django.urls import path,include
from home import views


admin.site.site_header = "SUBMAN APP DB"
admin.site.site_title = "SUBMAN Admin Portal"
admin.site.index_title = "Welcome to SUBMAN Portal"

urlpatterns = [
   path("index", views.index , name='index'),
   path("home", views.home , name='home'),
   path("about", views.about , name='about'),
   path("services", views.services , name='services'),
   path("contact", views.contact , name='contact')
]
