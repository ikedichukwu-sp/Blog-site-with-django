from app.models import Article
from django.shortcuts import render
from app.forms import CreateArticleForm
from django.shortcuts import render, redirect


def home(request):
    articles = Article.objects.all()
    return render(request, "home.html", {"articles": articles})


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