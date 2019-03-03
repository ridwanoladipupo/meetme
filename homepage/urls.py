from django.urls import include, path

from .views import CreateViewHome


urlpatterns = [
    path('', CreateViewHome, name='home'),
    path('', include('signup.urls')),
    path('', include('login.urls')),
    path('', include('main.urls')),
    
]
