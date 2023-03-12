from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import House
from rest_framework.views import APIView
from .serializers import HouseSerializer


class HouseListAPI(APIView):
    def get(self, request):
        queryset = House.objects.all()
        serializer = HouseSerializer(queryset, many=True)
        return Response(serializer.data)


class CrawlingAPI(APIView):
    def get(self, request):
        return Response()


def testFunc():
    arr = []
    for i in range(10):
        arr.append(i)
    return arr
