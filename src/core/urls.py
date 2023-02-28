from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import (
    TownView, HouseView, PersonView
)

urlpatterns = [
    path('municipios/', TownView.as_view()),
    path('municipios/<int:id>', TownView.as_view()),
    path('viviendas/', HouseView.as_view()),
    path('viviendas/<int:id>', HouseView.as_view()),
    path('personas/', PersonView.as_view()),
    path('personas/<int:id>', PersonView.as_view())
]