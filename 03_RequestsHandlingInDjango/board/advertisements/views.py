from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


class Regions(View):
    region = (
        'Москва',
        'Московская область',
        'республика Алтай',
        'Вологодская область'
    )
    count = 0

    def get(self, request):
        Regions.count += 1
        return render(request, 'advertisements/first.html', {'region': Regions.region})

    def post(self, request):
        return render(request, 'advertisements/second.html', {'count': Regions.count})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['address'] = 'г.Москва, ул.Ленина 1'
        context['number'] = '8-977-777-77-77'
        context['email'] = '1@mail.ru'
        return context


class About(TemplateView):
    template_name = "advertisements/about.html"

    def get_context_data(self, *args, **kwargs):
        context = super(About, self).get_context_data(*args, **kwargs)
        context["name"] = "Бесплатные объявления в вашем городе"
        context["title"] = "Бесплатные объявления"
        context["description"] = """
        Если вы хотите продать или купить чтото быстро, к вашим услугам наша доска объявлений
        """
        return context


class Main(View):
    category = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]

    region = [
        'Москва',
        'Московская область',
        'республика Алтай',
        'Вологодская область'
    ]

    def get(self, request):
        return render(request, 'advertisements/main.html', {'category': Main.category, 'region': Main.region})

    def post(self, request):
        category = {request.POST['categor']}
        region = {request.POST['reg']}
        name = {request.POST['name_adv']}
        return render(request, 'advertisements/main_post.html', {'category': category, 'region': region, 'name': name})
