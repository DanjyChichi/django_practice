from django.shortcuts import render
from .models import Member


def index(request):
    members = Member.objects.all().order_by('-pk')

    return render(
        request,
        'index.html',
        {
            'members' : members,
        }
    )