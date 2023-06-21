from django.urls import path
from . import views
urlpatterns = [
    #127.0.0.1:8000/blog/2/
    path('<int:value>/',	views.single_post_page),
    path('',views.index),
]