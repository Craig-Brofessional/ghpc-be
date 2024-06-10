from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Pushup(models.Model):
    user_id = models.IntegerField(primary_key=True)
    balance = models.IntegerField(default=0)
    datetime_updated = models.DateTimeField("datetime updated", auto_now=True)