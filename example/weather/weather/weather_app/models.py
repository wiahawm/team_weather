from django.db import models

# Create your models here.
class TeamWeather(models.Model):
    id = models.IntegerField(primary_key=True) 
    city = models.TextField()
    sky = models.TextField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    humidity = models.FloatField()
    created_at = models.TextField()
    temp = models.FloatField()
    feels_like = models.FloatField()

    class Meta:
        managed = False
        db_table = 'team_weather'