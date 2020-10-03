from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll, name='poll'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('result/<poll_id>/', views.result, name='result'),
    path('create', views.create, name='create'),

]