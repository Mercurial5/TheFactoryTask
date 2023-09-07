from django.urls import path

from . import views

urlpatterns = [
    path('generate-token/', views.generate_token),
    path('send/', views.send)
]