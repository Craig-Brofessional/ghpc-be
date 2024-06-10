from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Pushup
from ghpc.serializers import PushupSerializer


# Create your views here.

class PushupsApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'user_id': request.data.get('user_id'),
        }
        serializer = PushupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PushupsDetailApiView(APIView):

    def get(self, request, user_id, *args, **kwargs):        
        pushup = Pushup.objects.get(user_id=user_id)
        serializer = PushupSerializer(pushup)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        # print('user_id: ', user_id)
        # print('request: ', request)
        # print('args: ', args)
        # print('kwargs: ', kwargs)

        amount = request.data.get('amount')

        if amount is None or not isinstance(amount, int):
            return Response('Invalid amount', status=status.HTTP_400_BAD_REQUEST)
        
        pushup = Pushup.objects.get(user_id=user_id)
        if not pushup:
            return Response("Pushup balance not found", status=status.HTTP_400_BAD_REQUEST)
        
        pushup.balance += amount
        pushup.save()
        
        serializer = PushupSerializer(pushup)
        return Response(serializer.data, status=status.HTTP_200_OK)
