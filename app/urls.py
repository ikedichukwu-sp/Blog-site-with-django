from django.urls import path
from app.views import home, ArticleCreateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("articles/create/", ArticleCreateView.as_view(), name="create_article")
]
