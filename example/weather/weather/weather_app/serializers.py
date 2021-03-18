# serializers.py 

from weather.weather_app.models import TeamWeather
from rest_framework import serializers

class MyTopicUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamWeather
        fields = ['id', 'city', 'temp_min','temp_max','humidity', 'created_at','temp','feels_like']

        read_only_fields = ('id', 'city', 'temp_min','temp_max','humidity', 'created_at','temp','feels_like')
