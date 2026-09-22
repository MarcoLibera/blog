from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.index, name='index'),    # Route the root URL of posts apps to index view. I.e. all requests to /posts/ will be handled by the index view.
    path('post/<int:post_id>/', views.get_post, name='get_post')
    # path('test_form', views.test_form, name='test_form')
]

