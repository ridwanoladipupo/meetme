from django.urls import include, path

from .views import CreateViewMain


app_name = 'main'

urlpatterns = [
    path('main/', CreateViewMain, name='main'),
]
