from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import base64

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from weather.weather_app.models import TeamWeather
from weather.weather_app.serializers import MyTopicUsersSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class MyTopicUsersViewSet(viewsets.ModelViewSet):
    queryset = TeamWeather.objects.all()
    serializer_class = MyTopicUsersSerializer
    
    permission_classes = [permissions.IsAuthenticated]

    # /my_topic_users/search?q=?
    @action(detail=False, methods=['GET'])
    def search(self, request):
        q = request.query_params.get('q', None)

        qs = self.get_queryset().filter(city=q)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def coordination(self, request):
        clothes = [
            {'minT':-10, 'maxT':-5, 'type':'outer', 'name':'패딩'},
            {'minT':-10, 'maxT':-5, 'type':'bottom', 'name':'기모바지'},
            {'minT':-10, 'maxT':-5, 'type':'add', 'name':'귀마개'},
            {'minT':-5, 'maxT':0, 'type':'add', 'name':'장갑'},
            {'minT':-5, 'maxT':0, 'type':'add', 'name':'핫팩'},
            {'minT':-5, 'maxT':0, 'type':'add', 'name':'목도리'},
            {'minT':0, 'maxT':5, 'type':'top', 'name':'히트텍'},
            {'minT':0, 'maxT':5, 'type':'bottom', 'name':'니트'},
            {'minT':0, 'maxT':5, 'type':'top', 'name':'두꺼운 목폴라'},
            {'minT':5, 'maxT':9, 'type':'outer', 'name':'조끼 패딩'},
            {'minT':5, 'maxT':9, 'type':'outer', 'name':'울코트'},
            {'minT':5, 'maxT':9, 'type':'top', 'name':'기모 후드티'},
            {'minT':9, 'maxT':12, 'type':'top', 'name':'셔츠'},
            {'minT':9, 'maxT':12, 'type':'outer', 'name':'트렌치코트'},
            {'minT':9, 'maxT':12, 'type':'bottom', 'name':'청바지'},
            {'minT':12, 'maxT':17, 'type':'outer', 'name':'가죽 자켓'},
            {'minT':12, 'maxT':17, 'type':'outer', 'name':'두꺼운 가디건'},
            {'minT':12, 'maxT':17, 'type':'bottom', 'name':'면바지'},
            {'minT':17, 'maxT':20, 'type':'top', 'name':'얇은 맨투맨'},
            {'minT':17, 'maxT':20, 'type':'outer', 'name':'얇은 가디건'},
            {'minT':17, 'maxT':20, 'type':'bottom', 'name':'얇은 청바지'},
            {'minT':20, 'maxT':23, 'type':'top', 'name':'블라우스'},
            {'minT':20, 'maxT':23, 'type':'bottom', 'name':'반바지'},
            {'minT':20, 'maxT':23, 'type':'bottom', 'name':'슬랙스'},
            {'minT':23, 'maxT':28, 'type':'top', 'name':'얇은 셔츠'},
            {'minT':23, 'maxT':28, 'type':'bottom', 'name':'통 넓은 바지'},
            {'minT':23, 'maxT':28, 'type':'add', 'name':'손선풍기'},
            {'minT':28, 'maxT':40, 'type':'shoes', 'name':'샌들'},
            {'minT':28, 'maxT':40, 'type':'bottom', 'name':'짧은 반바지'},
            {'minT':28, 'maxT':40, 'type':'add', 'name':'린넨 소재 옷'},
        ]

        q = request.query_params.get('q', None)
        qs = self.get_queryset().filter(city=q)
        serializer = self.get_serializer(qs, many=True)

        res = []
        for c in clothes:
            if c['minT'] <= serializer.data[-1]['feels_like'] < c['maxT']:
                res.append(c['name'])
        return Response({q:res})

    @action(detail=False, methods=['GET'])
    def music(self, request):
        music = [
            {'sky':'Thunderstorm', 'type':'dance', 'music':'Electric Shock - f(x)'},
            {'sky':'Drizzle', 'type':'pop', 'music':'Rain Drop - 아이유'},
            {'sky':'Rain', 'type':'hip-hop', 'music':'비도 오고 그래서 - 헤이즈'},
            {'sky':'Rain', 'type':'R&B', 'music':'비가 오는 날엔 - 비스트'},
            {'sky':'Snow', 'type':'pop', 'music':'Must have love - SG워너비 & 브라운아이드 걸스'},
            {'sky':'Mist', 'type':'ballad', 'music':'소나기 - 아이오아이'},
            {'sky':'Smoke', 'type':'OST', 'music':'Beautiful - Crush'},
            {'sky':'Haze', 'type':'R&B', 'music':'괜찮아도 괜찮아 - 디오(EXO)'},
            {'sky':'Dust', 'type':'R&B', 'music':'이 노랠 들어요 - 케이시'},
            {'sky':'Fog', 'type':'ballad', 'music':'거리에서 - 성시경'},
            {'sky':'Sand', 'type':'ballad', 'music':'서른 밤째 - 새봄'},
            {'sky':'Ash', 'type':'dance', 'music':'불꽃놀이 - 오마이걸'},
            {'sky':'Squall', 'type':'ballad', 'music':'우산 - 윤하'},
            {'sky':'Tornado', 'type':'dance', 'music':'Hurricane Venus - 보아'},
            {'sky':'Clear', 'type':'pop', 'music':'좋은날 - 아이유'},
            {'sky':'Clouds', 'type':'OST', 'music':'스며들기 좋은 오늘 - 백예린'}
        ]

        q = request.query_params.get('q', None)
        qs = self.get_queryset().filter(city=q)
        serializer = self.get_serializer(qs, many=True)

        res = []
        for m in music:
            if serializer.data[-1]['sky'] == m['sky']:
                res.append(m['music'])
        return Response({q:res})

    @action(detail=False, methods=['GET'])
    def thi(self, request): # 불쾌지수 (Temperature Humidity Index)
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)

        chk = 0
        res = []
        for data in serializer.data[-7:]:
            if data['humidity'] > chk:
                chk = data['humidity']
                thi = (1.8 * data['temp']) - (0.55 * (1 - (data['humidity'] / 100)) * (1.8 * data['temp'] - 26)) + 32
                res.append({'지역': data['city'], '기온': data['temp'], '습도': data['humidity'], '불쾌지수': round(thi, 2), '날짜': data['created_at']})
        return Response({'불쾌지수 가장 높은 지역 정보' : res[-1]})

    @action(detail=False, methods=['GET'])
    def chart(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        post_df = pd.DataFrame(list(serializer.data[-7:]))
        plt.bar(post_df['city'], post_df['temp_max'])
        plt.savefig('temp_max.png')
        return Response({'temp_max':'성공'})