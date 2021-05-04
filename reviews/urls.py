from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_review, name='submit_review'),
]