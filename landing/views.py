from django.shortcuts import render


def index(request):
    res = render(request, 'landing/home.html')
    return res

def price(request):
    res = render(request, 'landing/price.html')
    return res

def terms(request):
    res = render(request, 'landing/terms.html')
    return res

def privacy(request):
    res = render(request, 'landing/privacy.html')
    return res

def contacts(request):
    res = render(request, 'landing/contacts.html')
    return res
