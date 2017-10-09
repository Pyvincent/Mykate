# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from kate.models import Person


def handler404(request):
    return render(request, '404.html')


def handler500(request):
    return render(request, '500.html')


def handler403(request):
    return render(request, '403.html')


def ulist(request):
    Class = Person.objects.all().order_by('-name')
    # Class = Person.objects.all()[:1]

    return render(request, 'kate/ulist.html', {"Class": Class})
