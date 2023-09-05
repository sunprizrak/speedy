from django.urls import path
from .views import HomeView, AboutUs, Games

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutUs.as_view(), name='about'),
    path('games', Games.as_view(), name='games'),
]