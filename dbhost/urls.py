from django.urls import path

from . import views

urlpatterns = [
    path('kakaomap/', views.kakaoMap, name='kakaomap'),

]