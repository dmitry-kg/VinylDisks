

from django.urls import path
from .views import inquiri
urlpatterns = [
    path('inquiri', inquiri, name = 'inquiri'),

]
