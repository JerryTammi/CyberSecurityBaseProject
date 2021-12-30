from django.urls import path
from .views import create_ad, list_ads, buy, personal_list, delete
from accounts.views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('createad/', create_ad, name='ad'),
    path('listads/', list_ads, name='list_ads'),
    path('buy/', buy, name='buy'),
    path('delete/', delete, name='delete'),
    path('user/<int:id>/list', personal_list, name='personal_list'),
]