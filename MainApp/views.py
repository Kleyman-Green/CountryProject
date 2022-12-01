from django.shortcuts import render
import json
from MainApp.models import Country
from string import ascii_uppercase

# CountryJson = list(json.load(open('country-by-languages.json')))
# countrylist = [i.get("country") for i in CountryJson]
# languagelist = [i.get("languages") for i in CountryJson]
# modelscountry = (list(zip(countrylist, languagelist)))
#
# [Country(i, country[0], "_".join(country[1])).save() for i, country in enumerate(modelscountry, start=1)]

def country_list(request):
    context = {"countries": sorted([i.name for i in Country.objects.all()])}
    return render(request, "country-list.html", context)

def language_list(request):
    tmp = []
    for country in Country.objects.all():
        [tmp.append(i) for i in country.languages.split("_")]
    context = {"languages": sorted(set(tmp))}
    return render(request, "language-list.html", context)

def country-list-letter
def country_page(request, country_name:str):
    context = {'country': country_name, "languages": [i.languages for i in Country.objects.filter(name= country_name)][0].split("_")}
    context["letters"]= list(ascii_uppercase)
    return render(request, "country-page.html", context)

def language_page(request, language_name:str):
    context = {'language': language_name, "countries": [i.name for i in Country.objects.all() if language_name in i.languages.split("_")]}
    return render(request, "language-page.html", context)

def home(request):
    return render(request, "home.html")

