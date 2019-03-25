from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from .models import Modern, Origin, Language, Region

def index(request):
    return render(request, 'etym/index.html')

def search_terms(search_term):
    return Modern.objects.filter(
        Q(modern_word__icontains=search_term) | 
        Q(region__name__icontains=search_term) | 
        Q(language__name__icontains=search_term) | 
        Q(origin__word__icontains=search_term)
    )

def search(request):
    search_term = request.GET.get('query', '')
    terms = search_terms(search_term)
    return render(request, 'etym/search.html', {'terms': terms})

def search_json(request):
    search_term = request.GET.get('query', '')
    terms = search_terms(search_term)

    regions = {}
    
    for term in terms:
        if term.region.name not in regions.keys():
            regions[term.region.name] = []

        related_words = []
        for word in term.region.modern_set.all():
            if word.modern_word != term.modern_word:
                related_words.append(word.modern_word)

        regions[term.region.name].append({
            'modern_word': term.modern_word,
            'related_words': related_words,
            'region': term.region.name,
            'language': term.language.name,
            'word': term.origin.word,
            'meaning': term.origin.meaning,
            'coordinates': { 
                'lat': term.region.geolocation.lat,
                'lng': term.region.geolocation.lon,
            },
        })

    return JsonResponse({'results': regions})
    