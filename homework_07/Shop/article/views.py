from django.shortcuts import render
from .models import Group



# Create your views here.


def start_page(request):
    all_groups = Group.objects.all()

    context = {
        'all_groups': all_groups
    }

    return render(request, 'start_page.html', context=context)



