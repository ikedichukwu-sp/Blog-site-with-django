from app.models import Article
from django.shortcuts import render
# from app.forms import CreateArticleForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ArticleListView(ListView):
    template_name = "home.html"
    model = Article
    context_object_name = "articles"


""" this a function base view for the home
def home(request):
    articles = Article.objects.all()
    return render(request, "home.html", {"articles": articles})
"""


# using class base view, django will create the form automatically
class ArticleCreateView(CreateView):
    template_name = "article_create.html"
    model = Article
    fields = ["title", "status", "content",  "twitter_post"]
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    template_name = "article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "articles"


class ArticleDeleteView(DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "articles"


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
