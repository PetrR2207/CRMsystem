from django.urls import path
from . import views

app_name = 'personal_account_admin'

urlpatterns = [
    path('', views.auth, name='auth'),
]