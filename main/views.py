from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Categories

def index(request):
    context = {
        'title': 'LL',
        'content': 'L library',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'LL - О нас',
        'content': "О нас",
        'text_on_page': "Текст о нас"
    }

    return render(request, 'main/about.html', context)
