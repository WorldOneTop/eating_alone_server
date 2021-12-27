from django.urls import path

from . import views

urlpatterns = [
    path('kakaomap/', views.kakaoMap),
    path('firebase/', views.firebase),
    path('checkId/',views.checkId),
    path('login/',views.login),
    path('signUp/',views.signUp),
    path('accoutOut/',views.accoutOut),
    path('updateNickname/',views.updateNickname),
    path('updateImage/',views.updateImage),
    path('updatePassword/',views.updatePassword),
    path('findAccount/',views.findAccount),
    path('selectMyReview/',views.selectMyReview),
    path('selectMyHouse/',views.selectMyHouse),
    path('selectUserInfo/',views.selectUserInfo),
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
    path('selectHouseName/',views.selectHouseName),
    path('selectHouseInfo/',views.selectHouseInfo),
    path('selectHouseMenu/',views.selectHouseMenu),
    path('selectHouseReview/',views.selectHouseReview),
    path('selectNotice/',views.selectNotice),
]