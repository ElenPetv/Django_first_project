from django.shortcuts import render

# Create your views here.
import json

from .models import Library

from django.http import HttpResponse


def get_books(request):
    library = list(Library.objects.all())
    context = {
        'Library': library
    }
    content = json.dumps(context, indent=4, sort_keys=True, default=str)
    return HttpResponse(f'<h2 style="color: #2f90cc; margin: 20px;">{content}</h2>')
