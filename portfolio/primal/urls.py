from django.urls import path

from . import views

urlpatterns = [
    path("primal/", views.primal, name="primal"),
    path("episodios/", views.episodios, name="episodios"),
    path("extras/", views.extras, name="extras"),
    path("perfil/", views.perfil, name="perfil"),
    path("personajes/", views.personajes, name="personajes"),
]