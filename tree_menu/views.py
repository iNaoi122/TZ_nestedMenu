from django.shortcuts import render
from .models import Branch


# Create your views here.

def menu_view(request):
    listing = Branch.objects.filter(parent=None)
    context = {'listing': listing}
    return render(request, 'menu.html', context)
