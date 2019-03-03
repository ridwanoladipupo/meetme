from django.urls import path

from .views import CreateViewSignup


app_name = 'signup'

urlpatterns = [
   path('signup/', CreateViewSignup, name='signup'),
]
