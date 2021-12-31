from django.urls import path

from . import views

app_name = 'uploads'

urlpatterns = [
    path('',views.index,name='index'),
    path('author/',views.author, name='author'),
    path('book/',views.book, name='book'),
]