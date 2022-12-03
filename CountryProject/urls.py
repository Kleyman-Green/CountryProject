
from django.contrib import admin
from django.urls import path
from MainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('country-list/', country_list),
    path("language-list/", language_list),
    path('country-page/<country_name>', country_page),
    path('language-page/<language_name>', language_page),
    path('country-list-letter/<letter_name>', country_list_letter),
    path('languages-list-letter/<letter_name>', language_list_letter),
]
