from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomeView, AboutView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
]