from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Categories

def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'LL',
        'content': 'L library',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'LL - О нас',
        'content': "О нас",
        'text_on_page': "Текст о нас"
    }

    return render(request, 'main/about.html', context)
