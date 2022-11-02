from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import ArticleRegistrationForm, ArticleUpdateForm, LoginForm
from .models import Article

# Function to render Homepage
def home(request):
    article_list = Article.objects.all()
    return render(request, 'home.html', {'article_list':article_list})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("You are authenticated")


            else:
                return HttpResponse("Invalid Login")


    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form':form})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

@login_required
def article_form(request):

    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')

    else:
        article_form = ArticleRegistrationForm()

    return render(request, 'account/add_article.html', {'article_form':article_form})

def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')

    return render(request, 'account/update.html', {'form':form})

def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('article_list')
