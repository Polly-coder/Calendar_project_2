from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', db_index=True, max_length=64)
    date = models.DateTimeField(verbose_name='Date')
    user = models.ForeignKey(User,verbose_name='User', on_delete=models.CASCADE)
    guest = models.EmailField(verbose_name='guest')