# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Review, Image, House_main, House_detail, House_menu, Question


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getKakaoMapKey():
    with open(BASE_DIR+'/secret.json', 'r') as f:
        jf = json.load(f)
    return jf['KAKAOMAP_API_KEY']

def kakaoMap(request):
    getValue = {}

    getValue['key'] = getKakaoMapKey()

    getValue['width'] = request.GET['width']
    getValue['height'] = request.GET['height']
    getValue['centerLat'] = request.GET['centerLat']
    getValue['centerLng'] = request.GET['centerLng']
    getValue['zoomLevel'] = request.GET['zoomLevel']
    getValue['hasListener'] = request.GET['hasListener']

    return render(request, 'dbhost/kakaomap.html',getValue);


    """     ACCOUNT     """
def login(request):
    return HttpResponse("OK")

def logout(request):
    return HttpResponse("OK")

def signUp(request):
    User.objects.create(request.GET)
    return HttpResponse("OK")

def accoutOut(request):#회원탈퇴
    return HttpResponse("OK")

def updateNickname(request):
    return HttpResponse("OK")

def updateImage(request):
    return HttpResponse("OK")

def updatePassword(request):
    return HttpResponse("OK")

def findAccount(request):
    return HttpResponse("OK")

def selectMyReview(request):
    return HttpResponse("OK")

def selectMyHouse(request):
    return HttpResponse("OK")


    """     QUESTION    """
def createQnA(request):
    return HttpResponse("OK")

def selectMyQuestion(request):
    return HttpResponse("OK")

def selectFAQ(request):
    return HttpResponse("OK")


    """     REVIEW      """
def createReview(request):
    return HttpResponse("OK")

def deleteReview(request):
    return HttpResponse("OK")


    """     HOUSE       """
def createHouse(request):
    return HttpResponse("OK")

def updateHouse(request):
    return HttpResponse("OK")

def selectCategoryHouse(request):
    return HttpResponse("OK")

def selectLocationHouse(request):
    return HttpResponse("OK")

def selectSearchHouse(request):
    return HttpResponse("OK")

def selectDetailHouse(request):
    return HttpResponse("OK")

def selectMenuHouse(request):
    return HttpResponse("OK")

def selectReivewHouse(request):
    return HttpResponse("OK")


    """     NOTICE      """
def selectNotice(request):
    return HttpResponse("OK")


