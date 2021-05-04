from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_review_page, name='submit_review_page'),
    path('submit_review/', views.submit_review, name='submit_review'),
]