from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionDenied
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import user_passes_test
from app_users.forms import AuthForm, RegisterForm, NewsForm, CommentForm
from app_users.models import Profile, News, Comment
from django import forms


def create_groups(request):
    if not Group.objects.filter(name='Обычные пользователи').exists():
        Group.objects.create(name='Обычные пользователи')
    if not Group.objects.filter(name='Верифицированные пользователи').exists():
        Group.objects.create(name='Верифицированные пользователи')
    if not Group.objects.filter(name='Модераторы').exists():
        Group.objects.create(name='Модераторы')
    return HttpResponse("<h3>Необходимые группы пользователей были успешно созданы, либо уже существуют</h3>"
                            "<h3><a href='/news_list'>Страница новостей</a></h3>")


class UserVerView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'app_users/users.html'
    context_object_name = 'users'
    queryset = User.objects.filter(groups__name__icontains='пользователи')

    def test_func(self):
        return self.request.user.groups.filter(name='Модераторы').exists()

    def post(self, request):
        user = User.objects.get(id=request.POST.get('user.id'))
        user.groups.clear()
        if request.POST.get('user.profile.verification') == 'True':
            group = Group.objects.get(name='Верифицированные пользователи')
            user.profile.verification = True
        elif request.POST.get('user.profile.verification') == 'False':
            group = Group.objects.get(name='Обычные пользователи')
            user.profile.verification = False
        user.groups.add(group)
        user.profile.save()
        user.save()
        return redirect('users')





class MainView(View):
    def get(self, request):
        print(request.user.groups.filter(name='Модераторы').exists())
        return render(request, 'app_users/main.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            number = form.cleaned_data.get('number')
            city = form.cleaned_data.get('city')
            Profile.objects.create(user=user, number=number, city=city)
            group = Group.objects.get(name='Обычные пользователи')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main')
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'app_users/login.html'

class LogoutView(LogoutView):
    template_name = 'app_users/logout.html'
    next_page = 'main'


class NewsView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moder'] = self.request.user.groups.filter(name='Модераторы').exists()
        context['user'] = self.request.user.is_authenticated
        return context


    def post(self, request):
        if not request.user.groups.filter(name='Модераторы').exists():
            raise PermissionDenied()
        new = self.model.objects.get(id=request.POST.get('news.id'))
        new.is_active = request.POST.get('news.is_active')
        new.save()
        return redirect('news_list')

        # request.user.groups.filter(name__in=['Обычные пользователи', 'Верифицированные пользователи', 'Модераторы']).exists()

class NewsDetailView(DetailView):
    model = News
    template_name = 'app_users/news_detail.html'
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
                user_1 = request.user.first_name + ' ' + request.user.last_name
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
            return render(request, 'app_users/create_comment.html',
                              context={'comment_form': comment_form, 'news': news, 'news_id': news_id})


class CreateNewsView(UserPassesTestMixin, CreateView):
    form_class = NewsForm
    template_name = 'app_users/create.html'
    success_url = reverse_lazy('news_list')

    def test_func(self):
        return self.request.user.profile.verification


    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_form'] = NewsForm()
        self.request.user.profile.count_news += 1
        self.request.user.profile.save()
        return context


