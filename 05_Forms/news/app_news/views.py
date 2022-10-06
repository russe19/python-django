from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from app_news.models import News, Comment
from app_news.forms import NewsForm, CommentForm
from django.http import HttpResponse
from django import forms


class NewsView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()

class NewsDetailView(DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.filter(news_name=kwargs['object'])
        return context

    def post(self, request, news_id):
        if request.POST.get('text'):
            comment_form = CommentForm(request.POST)
            if request.user.is_authenticated:
                comment_form.fields['user_name'].required = False
                user_1 = request.user.username
            else:
                user_1 = request.POST['user_name'] + '(Аноним)'
            if comment_form.is_valid():
                comment = Comment(user_name=user_1,
                                  text = request.POST['text'], news_name = News.objects.get(id=news_id))
                comment.save()
                return redirect('news_list')
        else:
            comment_form = CommentForm()
            if request.user.is_authenticated:
                comment_form.fields['user_name'].widget = forms.HiddenInput()
            news = str(News.objects.get(id=news_id))
            return render(request, 'app_news/create_comment.html',
                              context={'comment_form': comment_form, 'news': news, 'news_id': news_id})


class CreateNewsView(CreateView):
    form_class = NewsForm
    template_name = 'app_news/create.html'
    success_url = reverse_lazy('news_list')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_form'] = NewsForm()
        return context

class UpdateNewsView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'app_news/update.html'
    success_url = reverse_lazy('news_list')

class Main(View):
    def get(self, request):
        return render(request, 'app_news/main.html')

class ViewLogin(LoginView):
    template_name = 'app_news/login.html'

class ViewLogout(LogoutView):
    template_name = 'app_news/logout.html'
    next_page = 'main'





