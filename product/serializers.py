from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer) :
    class Meta:
        model = House        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함