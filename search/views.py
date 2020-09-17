from django.shortcuts import render
from django.http import JsonResponse

import wikipedia

def index(request):
    wiki = wikipedia.summary("Wikipedia")
    search = wikipedia.search("Judas Iscariot")
    print(search)
    return JsonResponse({
        # 'wiki': wiki,
        'search': search
    })

def phone_verify(request):
    pass
