from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})

def advertisement_1(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_1.html', {})

def advertisement_2(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_2.html', {})

def advertisement_3(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_3.html', {})

def advertisement_4(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_4.html', {})

def advertisement_5(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_5.html', {})

