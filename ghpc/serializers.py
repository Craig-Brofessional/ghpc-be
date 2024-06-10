from rest_framework import serializers
from .models import Pushup

class PushupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pushup
        fields = ["user_id", "balance", "datetime_updated"]