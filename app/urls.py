from django.urls import path
# from django.contrib.auth import views as auth_views
from app.views import ArticleCreateView, ArticleDeleteView, ArticleUpdateView, ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),  # Home page shows list of articles
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article"),
    # path("accounts/login/", auth_views.LoginView.as_view(), name="login"),  # Add this for logi

]

