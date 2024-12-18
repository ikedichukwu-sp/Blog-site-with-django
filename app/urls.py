from django.urls import path
from app.views import home, create_article
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("articles/create/", create_article, name="create_article")
]
