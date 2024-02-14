from django.shortcuts import render, redirect
from item import models
from . import forms


def index(request):
    items = models.Item.objects.filter(is_sold=False)[0:8]
    categories = models.Category.objects.all()
    return render(request, 'core/index.html', context={'categories': categories,
                                                       'items': items})


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.SignupForm()

    return render(request, template_name='core/signup.html', context={'form': form})