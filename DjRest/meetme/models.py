from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', db_index=True, max_length=64)
    user = models.ForeignKey(User,verbose_name='User', on_delete=models.CASCADE)
    guest = models.EmailField(verbose_name='guest')

class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, verbose_name='Event', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Date')
    time = models.TimeField(verbose_name='Start')