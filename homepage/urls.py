from django.urls import path

from .views import CreateViewHome

urlpatterns = [
    path('', CreateViewHome, name='home'),
]
