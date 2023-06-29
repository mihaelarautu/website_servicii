from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('Acasa/', views.homepage, name='home_page'),
    path('Servicii/', views.services, name='services'),
    path('Servicii/Formular-de-contact/', views.contact_form_view, name='contact_form'),
    path('Contact/', views.contact, name='contact'),
    path('Formular-de-contact/', views.contact_form_view, name='contact_form'),
    path('Blog/', views.blog, name='blog'),
    path('Politica-de-confidentialitate/', views.confidentiality, name='confidentiality'),
    path('<base/', views.blog_post, name='title'),
    path('check_post', views.check_post, name='check_post'),
    path('add_post', views.add_post, name='ad_post'),
    path('get_posts/<str:blog_post>/', views.get_posts, name='get_posts')
]
