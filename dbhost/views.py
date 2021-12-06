# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import string
import random
from django.db import IntegrityError

from .models import User, Review, Image, House_main, House_detail, House_menu, Question


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''  다 하고 할거 : select 처리, 이미지 처리, 문자 보내기 처리  '''



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
def checkUserFormatId(data):
    return data.isdigit() and (10 <= len(data) and len(data) < 12)
def checkUserFormatPw(data):
    return len(data) == 64
def checkUserFormatNick(data):
    return 1 <= len(data) and len(data) < 11
def checkUserFormatImg(data):
    return 1 <= len(data) and len(data) < 20


def login(request): # args : id, password
    data = request.GET.dict()
    try:
        login_user = User.objects.get(pk=data['id'])
        if(login_user.password != data['password']):
            return HttpResponse('비밀번호가 일치하지않습니다.')
    except User.DoesNotExist:
        return HttpResponse('해당 아이디가 존재하지않습니다.')
    except KeyError:
        return HttpResponse('data is not enough')
    return HttpResponse()

def signUp(request): # args : id, password, nickName
    data = request.GET.dict()
    try:
        if(not checkUserFormatId(data['id'])):
            return HttpResponse('phone number format mismatch')
        if(not checkUserFormatPw(data['password'])):
            return HttpResponse('password format mismatch')
        if(not checkUserFormatNick(data['nickName'])):
            return HttpResponse('nickname is to long or empty')
    except KeyError:
        return HttpResponse('data is not enough')
    try:
        User.objects.create(**data)
    except IntegrityError:
        return HttpResponse('이미 사용중인 아이디입니다.')
    return HttpResponse()

def accoutOut(request): # args : id, password
    checkUser = login(request)

    if(checkUser.content):
        return checkUser

    User.objects.get(pk=request.GET['id']).delete()
    return HttpResponse()

def updateNickname(request): # args : id, nickName
    data = request.GET.dict()

    if(not checkUserFormatNick(data['nickName'])):
        return HttpResponse('nickname is to long or empty')

    try:
        login_user = User.objects.filter(pk=data['id'])
    except User.DoesNotExist:
        return HttpResponse('해당 아이디가 존재하지않습니다.')


    login_user.update(nickName=data['nickName'])
    return HttpResponse()

def updateImage(request):
    pass
    return HttpResponse()

def updatePassword(request): # args : id, password, newPassword
    checkUser = login(request)

    if(checkUser.content):
        return checkUser

    data = request.GET.dict()

    if(not checkUserFormatPw(data['newPassword'])):
        return HttpResponse('password format mismatch')

    User.objects.filter(pk=data['id']).update(password=data['newPassword'])
    return HttpResponse()

def findAccount(request): # args : id
    try:
        user = User.objects.filter(pk=request.GET['id'])
    except User.DoesNotExist:
        return HttpResponse('해당 아이디가 존재하지않습니다.')

    # 랜덤 10자리(소문자+숫자) 문자열
    string_pool = string.ascii_lowercase + string.digits
    randomStr = ""
    for i in range(10) :
        randomStr += random.choice(string_pool)

    result = hashlib.sha256(randomStr.encode()).hexdigest()

    user.update(password=result)

    return HttpResponse('랜덤 문자열 : ' + randomStr + ' 번호로 보내기 처리 필요')

def selectMyReview(request):
    return HttpResponse()

def selectMyHouse(request):
    return HttpResponse()


    """     QUESTION    """
def createQnA(request):
    return HttpResponse()

def selectMyQuestion(request):
    return HttpResponse()

def selectFAQ(request):
    return HttpResponse()


    """     REVIEW      """
def createReview(request):
    return HttpResponse()

def deleteReview(request):
    return HttpResponse()


    """     HOUSE       """
def createHouse(request):
    return HttpResponse()

def updateHouse(request):
    return HttpResponse()

def selectCategoryHouse(request):
    return HttpResponse()

def selectLocationHouse(request):
    return HttpResponse()

def selectSearchHouse(request):
    return HttpResponse()

def selectDetailHouse(request):
    return HttpResponse()

def selectMenuHouse(request):
    return HttpResponse()

def selectReivewHouse(request):
    return HttpResponse()


    """     NOTICE      """
def selectNotice(request):
    return HttpResponse()


