from django.shortcuts import render, redirect, Http404
from django.contrib.auth.views import LoginView, LogoutView
from app_media.models import Profile, Entry, EntryImage
from app_media.forms import RegisterForm, RegisterFormUpdate, EntryForm, UploadFileForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, View, TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.views.generic.edit import FormView
from django.utils.translation import gettext as _
import datetime

class Login(LoginView):
    template_name = 'app_media/login.html'

class Logout(LogoutView):
    template_name = 'app_media/logout.html'
    next_page = 'entres'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'app_media/register.html'
    success_url = '/main'

    def form_valid(self, form):
        user = form.save()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        number = form.cleaned_data.get('number')
        city = form.cleaned_data.get('city')
        Profile.objects.create(user=user, number=number, city=city)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('/main')



class Update(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'app_media/update.html'
    success_url = reverse_lazy('main')
    fields = ['first_name', 'last_name', 'email']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = RegisterFormUpdate(instance=self.object.profile)
        return context

    def test_func(self):
        return self.request.user.id == self.kwargs['pk']

    def form_valid(self, form):
        profile_model = Profile.objects.get(user_id=self.object.id)
        profile_model.city = self.request.POST['city']
        profile_model.number = self.request.POST['number']
        profile_model.save()
        return super().form_valid(form)

class Main(ListView):
    model = Entry
    template_name = 'app_media/main.html'
    context_object_name = 'entres'
    queryset = Entry.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.request.user)

class EntryList(ListView):
    model = Entry
    template_name = 'app_media/entry_list.html'
    context_object_name = 'entres'
    queryset = Entry.objects.all().order_by('-created_at')


class EntryDetail(DetailView):
    model = Entry
    template_name = 'app_media/entry_detail.html'
    context_object_name = 'entry'


class UploadEntry(LoginRequiredMixin, FormView):
    form_class = EntryForm
    template_name = 'app_media/entry_create.html'
    success_url = '/main'

    def form_valid(self, form):
        entry = Entry.objects.create(user=self.request.user,
                                     name=self.request.POST['name'],
                                     description=self.request.POST['description'])
        for image in self.request.FILES.getlist('images'):
            entry_image = EntryImage.objects.create(entry=entry, image=image)
            entry_image.save()
        return redirect('/main')


class UploadFile(FormView):
    form_class = UploadFileForm
    template_name = 'app_media/upload_files.html'
    context_object_name = 'form'
    success_url = '/main'

    def form_valid(self, form):
        file = self.request.FILES['file']
        with file.open('r') as f:
            s = f.read().decode('utf-8')
            z = s.split('\n')
            t = [i[:-1].split(';') for i in z if i != '']
            for i in t:
                d = i[1].split(', ')
                Entry.objects.create(name=self.request.POST['name'],
                                     description=i[0],
                                     created_at=datetime.date(int(d[0]), int(d[1]), int(d[2])))

        return redirect('/entres')


