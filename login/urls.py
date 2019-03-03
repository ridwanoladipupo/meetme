from django.urls import path

from .views import CreateViewLogin #CreateViewLogout


app_name = 'login'

urlpatterns = [
    #path('logout/', CreateViewLogout, name='logout'),
    path('login/', CreateViewLogin.as_view(), name='login'),
]
