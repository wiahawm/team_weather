from django.shortcuts import render

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
    def serch(self, request):

        q = request.query_params.get('q', None)

        qs = self.get_queryset().filter(city=q)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)