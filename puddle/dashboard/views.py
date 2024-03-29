from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from item import models

@login_required
def index(request):
    items = models.Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', context={'items': items})

