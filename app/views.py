from typing import Any
from django.db.models.query import QuerySet


from app.models import Article
from django.shortcuts import render
# from app.forms import CreateArticleForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    return HttpResponse("Welcome to the homepage!")


class ArticleListView(LoginRequiredMixin, ListView):  # the LoginRequiredMixin ensure  user is login
    # before seeing the listview
    template_name = "home.html"
    model = Article
    context_object_name = "articles"

    """
    the bellow function ensure only the articles created by the user will be shown to the user
    """
    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


""" this a function base view for the home
def home(request):
    articles = Article.objects.all()
    return render(request, "home.html", {"articles": articles})
"""


# using class base view, django will create the form automatically
class ArticleCreateView(LoginRequiredMixin, CreateView):  # the LoginRequiredMixin ensure  user is login
    # before creating article
    template_name = "article_create.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # UserPassesTestMixin ensures only
    # the article creator can update it
    template_name = "article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "articles"

    # bellow code will check if the user is the creator of the article to be updated
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # UserPassesTestMixin ensures only
    # the article creator can delete it
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "articles"

    # bellow code will check if the user is the creator of the article to be updated
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator


"""  this is function base view that goes with form
def create_article(request):
    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_article = Article(
                title=form_data["title"],
                status=form_data["status"],
                content=form_data["content"],  # Ensure this matches the form field
                word_count=form_data["word_count"],
                twitter_post=form_data["twitter_post"],
            )
            new_article.save()
            return redirect("home")  # Redirect to the article list or another page
    else:
        form = CreateArticleForm()

    # Render the form for both GET and invalid POST requests
    return render(request, "article_create.html", {"form": form})
"""
