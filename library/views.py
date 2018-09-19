from django.shortcuts import render
from .models import Autor , Books
# Create your views here.


def index(request):
    data = Books.objects.order_by('name_book')
    context = {'Book': data}
    return render(request, 'library/index.html', context)
