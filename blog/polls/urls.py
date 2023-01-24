from django.urls import path
from .views import*

urlpatterns = [
    path('home/',home_page),
    path('catalog/',catalog_page),
    path('about/',about_page),
    path('contact/',contact_page),
    path('catalog-1/',part1),
    path('catalog-2/',part2),
    path('catalog-3/',part3)

]
