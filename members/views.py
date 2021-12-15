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

def member_detail_page(request, pk):
    member = Member.objects.get(pk=pk)

    return render(
        request,
        'members/member_detail_page.html',
        {
            'member' : member,
        }
    )


