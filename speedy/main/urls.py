from django.urls import path
from .views import HomeView, AboutUsView, PrivacyPolicyView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutUsView.as_view(), name='about'),
    path('<slug:slug>/privacy-policy', PrivacyPolicyView.as_view(), name='privacy_policy'),
]