from django.shortcuts import render

from kate.models import Person


# Create your views here.

def ulist(reuest):
    # Class = ['Chinese', 'English', 'Japanese']  # 列表
    Class = Person.objects.all().order_by('-name')
    # Class = Person.objects.all()[:1]

    return render(reuest, 'kate/index.html', {"Class": Class})
