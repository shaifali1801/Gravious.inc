from rest_framework import serializers
from .models import resident,federal , visitor

class residentSerializer(serializers.ModelSerializer):
    class Meta:
        model = resident
        fields = ['veh_id' , 'name' , 'apartment']
        
class fedralSerializer(serializers.ModelSerializer):
    class Meta:
        model = federal
        fields = ['veh_id']


class visitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = federal
        fields = ['veh_id' , 'name' , 'apartment','purpose','veh_type']