# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, CommentForm, UserLoginForm, CustomPasswordChangeForm, NewsForm
from .models import News, Comment


def home(request):
    latest_news = News.objects.order_by('-published_date')[:3]
    return render(request, 'main/home.html', {'latest_news': latest_news})


def contact(request):
    return render(request, 'main/contact.html')


def news_list(request):
    query = request.GET.get('query')
    order = request.GET.get('order', 'desc')
    if order == 'asc':
        news_list = News.objects.order_by('published_date')
    else:
        news_list = News.objects.order_by('-published_date')

    if query:
        news_list = news_list.filter(title__icontains=query)

    return render(request, 'main/news_list.html', {'news_list': news_list})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', news_id=news_id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(news=news)
    return render(request, 'main/news_detail.html', {'news': news, 'comments': comments, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    comments = Comment.objects.filter(user=request.user)

    return render(request, 'main/profile.html', {
        'password_form': password_form,
        'comments': comments,
    })


@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', news_id=news.id)
    else:
        form = NewsForm()
    return render(request, 'main/add_news.html', {'form': form})


@login_required
def edit_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', news_id=news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'main/edit_news.html', {'form': form, 'news': news})


@login_required
def delete_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'main/delete_news.html', {'news': news})
