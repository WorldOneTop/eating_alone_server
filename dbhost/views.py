# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.shortcuts import render


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
def login():
    pass
def logout():
    pass
def signUp():
    pass
def accoutOut():#회원탈퇴
    pass
def updateNickname():
    pass
def updateImage():
    pass
def updatePassword():
    pass
def findAccount():
    pass
def selectMyReview():
    pass
def selectMyHouse():
    pass


    """     QUESTION    """
def createQnA():
    pass
def selectMyQuestion():
    pass
def selectFAQ():
    pass


    """     REVIEW      """
def createReview():
    pass
def deleteReview():
    pass


    """     HOUSE       """
def createHouse():
    pass
def updateHouse():
    pass
def selectCategoryHouse():
    pass
def selectLocationHouse():
    pass
def selectSearchHouse():
    pass
def selectDetailHouse():
    pass
def selectMenuHouse():
    pass
def selectReivewHouse():
    pass


    """     NOTICE      """
def selectNotice():
    pass

