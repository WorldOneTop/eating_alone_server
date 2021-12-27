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

from .models import User, Review, Image, House_main, House_detail, House_menu, Question, Notice, Answer


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORY_MENU = ['한식', '분식', '카페', '일식', '치킨', '피자', '양식', '주식', '도시락', '패스트푸드', '기타']
CATEGORY_QUESTION = ['계정', '이용문의', '불편사항', '정보등록', '기타']

'''  할거 : 이미지 처리, 문자 보내기 처리  '''


"""     KAKAOMAP        """

def getKakaoMapKey():
    with open(BASE_DIR+'/secret.json', 'r') as f:
        jf = json.load(f)
    return jf['KAKAOMAP_API_KEY']

def kakaoMap(request):
    getValue = {}

    getValue['key'] = getKakaoMapKey()

    getValue['width'] = request.GET['width']
    getValue['height'] = request.GET['height']
    getValue['centerAddr'] = request.GET['centerAddr']
    getValue['zoomLevel'] = request.GET['zoomLevel']
    getValue['hasListener'] = request.GET['hasListener']
    getValue['hasClickListener'] = request.GET['hasClickListener']

    return render(request, 'dbhost/kakaomap.html',getValue);

def getFirebaseKey():
    with open(BASE_DIR+'/secret.json', 'r') as f:
        jf = json.load(f)

    result = {}
    for key, value in jf.items():
        if('FIREBASE' in key):
            result[key] = value
    return result

def firebase(request):
    return render(request, 'dbhost/firebase.html',getFirebaseKey());

    """     ACCOUNT     """
def checkUserFormatId(data):
    return data.isdigit() and (10 <= len(data) and len(data) < 12)
def checkUserFormatPw(data):
    return len(data) == 64
def checkUserFormatNick(data):
    return 1 <= len(data) and len(data) < 11
def checkUserFormatImg(data):
    return 1 <= len(data) and len(data) < 20


def checkId(request): # args : id
    try:
        User.objects.get(pk=request.GET['id'])
    except User.DoesNotExist:
        return HttpResponse()
    return HttpResponse('이미 가입한 아이디입니다.')

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

    return HttpResponse('랜덤 문자열 : ' + randomStr + ' ,번호로 보내기 처리 필요')

def selectMyReview(request): # args: id
    if(not request.GET['id']):
        return HttpResponse()
    objects = Review.objects.filter(user_id_fk=request.GET['id']).select_related('house_id_fk')

    result = []

    for obj in objects:
        result.append({'review_id': obj.id, 'body': obj.body, 'house_id': obj.house_id_fk_id, 'time': obj.time.strftime("%Y.%m.%d"), 'house_name': obj.house_id_fk.name})

    return HttpResponse(json.dumps(result, ensure_ascii=False)) # return: review_id, body, house_id, time,house_name

def selectMyHouse(request): # args: id,id,id,id, ...
    if(not request.GET['id']):
        return HttpResponse()

    result = []

    for id in request.GET['id'].split(','):
        result.append(House_main.objects.filter(pk=id).values('name', 'profile_image', 'category', 'rating', 'review_count', 'location')[0])
        result[-1]['rating'] = float(result[-1]['rating'])

    return HttpResponse(json.dumps(result, ensure_ascii=False)) # return: name, profile_image, category, rating, review_count, location

def selectUserInfo(request): # args: id
    if(not request.GET['id']):
        return HttpResponse()

    obj = User.objects.get(pk = request.GET['id'])
    result = {'nickName':obj.nickName,'image':obj.image}

    return HttpResponse(json.dumps(result, ensure_ascii=False)) # return: nickName, image

    """     QUESTION    """

def createQnA(request): # args: head, body, category, user_id, {image}
    data = request.GET.dict()

    try:
        data['user_id'] = User.objects.get(pk=data['user_id'])
    except User.DoesNotExist:
        return HttpResponse('해당 아이디가 존재하지않습니다.')

    if(data['category'] not in CATEGORY_QUESTION):
        return HttpResponse('카테고리를 올바르게 입력해주세요.')
    try:
        Question.objects.create(**data)
    except IntegrityError:
        return HttpResponse('data is not enough')
    return HttpResponse()

def selectMyQuestion(request): # args: id
    if(not request.GET['id']):
        return HttpResponse()

    objects = Question.objects.filter(user_id=request.GET['id'])
    result = []

    for obj in objects:
        result.append({'head':obj.head, 'body':obj.body, 'time':obj.time.strftime("%Y.%m.%d")})
        try:
            result[-1]['answer'] = Answer.objects.get(pk=obj.id)
        except Answer.DoesNotExist:
            pass

    return HttpResponse(json.dumps(result, ensure_ascii=False)) # return: head, body, time, answer_body

def selectFAQ(request): # args: category
    result = Question.objects.filter(category=request.GET['category'], user_id=None).values('head','body')[0]

    return HttpResponse(json.dumps(result, ensure_ascii=False)) # return: head, body


    """     REVIEW      """
def createReview(request): # args: user_id_fk, house_id_fk, body, rating, {hashtag}
    data = request.GET.dict()
    try:
        data['user_id_fk'] = User.objects.get(pk=data['user_id_fk'])
        data['house_id_fk'] = House_main.objects.get(pk=data['house_id_fk'])
    except User.DoesNotExist:
        return HttpResponse('user is does not exist')
    except House_main.DoesNotExist:
        return HttpResponse('restaurant is does not exist')
    try:
        Review.objects.create(**data)
    except IntegrityError:
        return HttpResponse('data is not enough')

    if(data['house_id_fk'].rating < 0):
        data['house_id_fk'].rating = 0
    elif(data['house_id_fk'].rating > 5):
        data['house_id_fk'].rating = 5

    data['house_id_fk'].rating = (data['house_id_fk'].rating * data['house_id_fk'].review_count + int(data['rating'])) / (data['house_id_fk'].review_count + 1)
    data['house_id_fk'].review_count += 1
    data['house_id_fk'].save()
    return HttpResponse()

def deleteReview(request): # args: id
    try:
        review = Review.objects.get(pk=request.GET['id'])
    except Review.DoesNotExist:
        return HttpResponse('review is does not exist')
    house = review.house_id_fk

    if(house.review_count - 1 == 0):
        house.rating = 0
    else:
        house.rating = (house.rating*house.review_count - review.rating) / (house.review_count - 1)
    house.review_count -= 1
    house.save()

    review.delete()

    return HttpResponse()


    """     HOUSE       """
def createHouse(request): # agrs: name, location, category, info, lat,lng, {time,number}
    data = request.GET.dict()
    data_main = {'name':data.pop('name'), 'location':data.pop('location'), 'category':data.pop('category')}

    if(data_main['category'] not in CATEGORY_MENU):
        return HttpResponse('카테고리를 올바르게 입력해주세요.')

    data['house_id_fk'] = House_main.objects.create(**data_main)
    try:
        House_detail.objects.create(**data)
    except IntegrityError:
        return HttpResponse('data is not enough')


    return HttpResponse()

def updateHouse(request): # args: id, {name, category, location,price_image_id, profile_image_id, lat, lng, info, number, time}
    data = request.GET.dict()
    try:
        data_detail = {'house_id_fk' : House_main.objects.get(pk=data['id'])}
    except User.DoesNotExist:
        return HttpResponse('해당 아이디가 존재하지않습니다.')

    if 'info' in data : data_detail['info'] = data.pop('info')
    if 'time' in data : data_detail['time'] = data.pop('time')
    if 'lat' in data : data_detail['lat'] = data.pop('lat')
    if 'lng' in data : data_detail['lng'] = data.pop('lng')
    if 'number' in data : data_detail['number'] = data.pop('number')

    if(len(data_detail) > 1):
        House_detail.objects.filter(pk=data['id']).update(**data_detail)

    if(len(data) > 1):
        House_main.objects.filter(pk=data['id']).update(**data)

    return HttpResponse()

def selectCategoryHouse(request): # agrs: category, location_1, {location_2, location_3}
    result = House_main.objects.filter(**(request.GET.dict())).values('id', 'rating', 'name', 'review_count', 'profile_image')
    for obj in result:
        obj['rating'] = float(obj['rating'])

    return HttpResponse(json.dumps((list(result)), ensure_ascii=False))# return: id, rating, name, review_count, profile_image

def selectLocationHouse(request): # agrs: {category}, location_1, {location_2, location_3}
    data = request.GET.dict()
    data['house_id_fk__location_1'] = data.pop('location_1')
    if 'location_2' in data:
        data['house_id_fk__location_2'] = data.pop('location_2')
    if 'location_3' in data:
        data['house_id_fk__location_3'] = data.pop('location_3')

    objects = House_detail.objects.select_related('house_id_fk').filter(**data)
    result = []

    for obj in objects:
        result.append({'id':obj.house_id_fk_id, 'rating':float(obj.house_id_fk.rating), 'name':obj.house_id_fk.name, 'review_count':obj.house_id_fk.review_count, 'profile_image':obj.house_id_fk.profile_image, 'lat':float(obj.lat), 'lng':float(obj.lng)})

    return HttpResponse(json.dumps((list(result)), ensure_ascii=False)) # return: id, rating, name, review_count, profile_image, lat, lng

def selectSearchHouse(request): # args: name, location_1, {location_2, location_3}
    data = request.GET.dict()
    data['name__contains'] = data.pop('name')

    result = House_main.objects.filter(**data).values('id', 'rating', 'name', 'review_count', 'category', 'profile_image')

    for obj in result:
        obj['rating'] = float(obj['rating'])

    return HttpResponse(json.dumps((list(result)), ensure_ascii=False)) # return: id, rating, name, review_count, category, profile_image

def selectHouseName(request): # args: location_1, {location_2, location_3}
    result = House_main.objects.filter(**(request.GET.dict())).values('name')
    return HttpResponse(json.dumps((list(result)), ensure_ascii=False)) # return: [name]

def selectHouseInfo(request): # args: id
    result = House_detail.objects.filter(pk=request.GET['id']).values('info', 'time', 'lat', 'lng', 'number')
    return HttpResponse(result) # return: info, time, lat, lng, number

def selectHouseMenu(request): # args: id
    if(not request.GET['id']):
        return HttpResponse()

    result = House_menu.objects.filter(house_id_fk=request.GET['id']).values('name', 'price', 'image')

    return HttpResponse(str(list(result))) # return: [name, price, image]

def selectHouseReview(request): # args: id
    if(not request.GET['id']):
        return HttpResponse()

    objects = Review.objects.filter(house_id_fk=request.GET['id']).select_related('user_id_fk')

    result = []

    for obj in objects:
        result.append({'user_id': obj.user_id_fk_id, 'user_image': obj.user_id_fk.image,'user_nickName': obj.user_id_fk.nickName, 'time': obj.time.strftime("%Y.%m.%d"), 'body': obj.body, 'hashtag': obj.hashtag, 'rating': float(obj.rating), 'images': obj.images})
    return HttpResponse(str(list(result))) # return: [user_id, user_image, user_nickName, time, body, hashtag, rating, images]


    """     NOTICE      """
def selectNotice(request): # args:
    result = Notice.objects.all().values('head', 'body', 'time')

    for obj in result:
        obj['time'] = obj['time'].strftime("%Y.%m.%d")

    return HttpResponse(json.dumps(list(result), ensure_ascii=False)) # return: head, body, time
