from django.urls import path

from uploads import views

app_name = 'uploads'

urlpatterns = [
    path('',views.index,name='index'),
]