from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import (
    MunicipioView, ViviendaView, PersonaView
)

urlpatterns = [
    path('municipios/', MunicipioView.as_view()),
    path('municipios/<int:id>', MunicipioView.as_view()),
    path('viviendas/', ViviendaView.as_view()),
    path('viviendas/<int:id>', ViviendaView.as_view()),
    path('personas/', PersonaView.as_view()),
    path('personas/<int:id>', PersonaView.as_view())
]