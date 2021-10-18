from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='myfirstapphome'),
    path('about/',views.about,name='myfirstappabout'),
    path('hndik/',views.hndik,name= 'myfirstapphndik')
]