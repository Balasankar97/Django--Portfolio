from django.conf import settings
from . import views
from django.urls import path

app_name='blog'

urlpatterns = [
    path('blogs',views.blog,name="blog"),
    path('<int:blog_id>',views.detail,name='detail'),
]