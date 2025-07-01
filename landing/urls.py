from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('price/', views.price, name="price"),
    path('terms/', views.terms, name="terms"),
    path('privacy/', views.privacy, name="privacy"),
    path('contacts/', views.contacts, name="contacts"),
]

# handler404 = 'landing.views.error_404_view'
