from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # Route the root URL of posts apps to index view. I.e. all requests to /posts/ will be handled by the index view.
]