from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact-api'),
    path('portfolio/', views.PortfolioList.as_view(), name='portfolio-list'),

]
