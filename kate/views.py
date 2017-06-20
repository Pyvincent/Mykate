# -*- coding:utf-8 -*-
from django.shortcuts import render

from kate.models import Person


def ulist(reuest):
    Class = Person.objects.all().order_by('-name')
    # Class = Person.objects.all()[:1]

    return render(reuest, 'kate/ulist.html', {"Class": Class})
