from django.urls import path

from . import views

urlpatterns = [
    path('kakaomap/', views.kakaoMap, name='kakaomap'),
    path('login/',views.login),
    path('signUp/',views.signUp),
    path('accoutOut/',views.accoutOut),
    path('updateNickname/',views.updateNickname),
    path('updateImage/',views.updateImage),
    path('updatePassword/',views.updatePassword),
    path('findAccount/',views.findAccount),
    path('selectMyReview/',views.selectMyReview),
    path('selectMyHouse/',views.selectMyHouse),
    path('createQnA/',views.createQnA),
    path('selectMyQuestion/',views.selectMyQuestion),
    path('selectFAQ/',views.selectFAQ),
    path('createReview/',views.createReview),
    path('deleteReview/',views.deleteReview),
    path('createHouse/',views.createHouse),
    path('updateHouse/',views.updateHouse),
    path('selectCategoryHouse/',views.selectCategoryHouse),
    path('selectLocationHouse/',views.selectLocationHouse),
    path('selectSearchHouse/',views.selectSearchHouse),
    path('selectDetailHouse/',views.selectDetailHouse),
    path('selectMenuHouse/',views.selectMenuHouse),
    path('selectReivewHouse/',views.selectReivewHouse),
    path('selectNotice/',views.selectNotice),
]