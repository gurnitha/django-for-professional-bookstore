# app/pages/urls.py
from django.urls import path
from app.pages.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]