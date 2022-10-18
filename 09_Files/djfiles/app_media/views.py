from django.shortcuts import render, redirect, Http404
from django.contrib.auth.views import LoginView, LogoutView
from app_media.models import Profile, Entry, EntryImage
from app_media.forms import RegisterForm, RegisterFormUpdate, EntryForm, UploadFileForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, View, TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
import datetime

class Login(LoginView):
    template_name = 'app_media/login.html'

class Logout(LogoutView):
    template_name = 'app_media/logout.html'
    next_page = 'entres'

def regist_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
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
            login(request, user)
            return redirect('/main')
    else:
        form = RegisterForm()
    return render(request, 'app_media/register.html', {'form': form})

class Update(UpdateView):
    model = User
    template_name = 'app_media/update.html'
    success_url = reverse_lazy('main')
    fields = ['first_name', 'last_name', 'email']
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["profile"] = RegisterFormUpdate(self.request.POST)
        else:
            context["profile"] = RegisterFormUpdate(instance=self.object.profile)
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['entres'] = Entry.objects.filter(user_id=self.request.user)
        return context

class EntryList(UserPassesTestMixin, ListView):
    model = Entry
    template_name = 'app_media/entry_list.html'
    context_object_name = 'entres'
    queryset = Entry.objects.all().order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = EntryImage.objects.values()
        return context

    def test_func(self):
        return not self.request.user.is_authenticated

class EntryDetail(DetailView):
    model = Entry
    template_name = 'app_media/entry_detail.html'
    context_object_name = 'entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imag'] = EntryImage.objects.values().filter(entry_id=self.object.pk)
        return context

def upload_entry(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EntryForm(request.POST, request.FILES)
            if form.is_valid():
                entry = Entry.objects.create(user=request.user,
                                             name=request.POST['name'],
                                             description=request.POST['description'])
                entry.save()
                for image in request.FILES.getlist('images'):
                    entry_image = EntryImage.objects.create(entry=entry, image=image)
                    entry_image.save()
                return redirect('/main')
        else:
            form = EntryForm()
        return render(request, 'app_media/entry_create.html', {'form': form})
    raise Http404()


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            with file.open('r') as f:
                s = f.read().decode('utf-8')
                print('\n', s, '\n')
                z = s.split('\n')
                t = [i[:-1].split(';') for i in z if i != '']
                print(t)
                for i in t:
                    d = i[1].split(', ')
                    Entry.objects.create(name = request.POST['name'],
                                         description = i[0],
                                         created_at = datetime.date(int(d[0]), int(d[1]), int(d[2])))

            return HttpResponse(content=[file.name, ' ', file.size, ' ', s1], status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'app_media/upload_files.html', context=context)



