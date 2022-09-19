from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from advertisements_app.models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]

class AdvertisementDetailView(DetailView):
    model = Advertisement

    def get_object(self):
        obj = super(AdvertisementDetailView, self).get_object()
        obj.views_count += 1
        obj.save()
        return obj
