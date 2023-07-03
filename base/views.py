from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Client,Product,Order,OrderDetails,TodayAmount
from .serializer import MyTokenObtainPairSerializer,ClientSerializer, OrderSerializer,ProductSerializer,OrderDetailsSerializer,TodayAmountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import json

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
        username=request.data["user"]['username'],
        email=request.data["user"]['email'],
        password=request.data["user"]['password']
    )
    user.is_active = True
    user.is_staff = True
    user.save()
    serializer = ClientSerializer(data=request.data["client"])
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([IsAuthenticated])
class ClientView(APIView):
    def get(self,request):
        allClients = ClientSerializer(Client.objects.all().order_by('fullName'),many=True).data
        for cli in allClients:
            try :
                cli['user'] = {'id':Client.objects.get(id=cli['id']).user.id,'username':Client.objects.get(id=cli['id']).user.username}
            except :
                cli['user'] = 'null'
        return Response(allClients)
    def post(self,request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        my_model = Client.objects.get(id=id)
        serializer = ClientSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = Client.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class ProductView(APIView):
    def get(self,request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        my_model = Product.objects.get(id=id)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = Product.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class OrderView(APIView):
    def get(self,request):
        allOrders = OrderSerializer(Order.objects.all().order_by('orderDate','orderTime'),many=True).data
        for ord in allOrders:
            ord['client'] = {'id':Order.objects.get(id=ord['id']).client.id, 'fullName':Order.objects.get(id=ord['id']).client.fullName, 'phoneNumber':Order.objects.get(id=ord['id']).client.phoneNumber, 'address':Order.objects.get(id=ord['id']).client.address}
        return Response(allOrders)
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            getid = Order.objects.filter(client_id=request.data["id"]).last().id
            data= request.data
            data["id"]= getid
            my_model = Order.objects.get(id=getid)
            serializer = OrderSerializer(my_model, data=request.data)
        except:
            my_model = Order.objects.get(id=id)
            serializer = OrderSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = Order.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class OrderDetailsView(APIView):
    def get(self,request):
        allOrderDetails = OrderDetailsSerializer(OrderDetails.objects.all(),many=True).data
        for orderDetails in allOrderDetails:
            orderDetails['order'] = {'id':OrderDetails.objects.get(id=orderDetails['id']).order.id,'orderDate':OrderDetails.objects.get(id=orderDetails['id']).order.orderDate, 'orderTime':OrderDetails.objects.get(id=orderDetails['id']).order.orderTime, 'orderStatus':OrderDetails.objects.get(id=orderDetails['id']).order.orderStatus, 'orderType':OrderDetails.objects.get(id=orderDetails['id']).order.orderType, 'payment':OrderDetails.objects.get(id=orderDetails['id']).order.payment, 
            'fullName':OrderDetails.objects.get(id=orderDetails['id']).order.client.fullName,'phoneNumber':OrderDetails.objects.get(id=orderDetails['id']).order.client.phoneNumber,'address':OrderDetails.objects.get(id=orderDetails['id']).order.client.address}
            orderDetails['product'] = {'id':OrderDetails.objects.get(id=orderDetails['id']).product.id, 'productName':OrderDetails.objects.get(id=orderDetails['id']).product.productName,'price':OrderDetails.objects.get(id=orderDetails['id']).product.price}
        return Response(allOrderDetails)
    def post(self,request):
        getid = Order.objects.filter(client_id=request.data["order"]).last().id
        data= request.data
        data["order"]= getid
        data["product"]= data["product"]["id"]
        serializer = OrderDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        my_model = OrderDetails.objects.get(id=id)
        serializer = OrderDetailsSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = OrderDetails.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class TodayAmountView(APIView):
    def get(self,request):
        my_model = TodayAmount.objects.all()
        serializer = TodayAmountSerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TodayAmountSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        my_model = TodayAmount.objects.get(id=id)
        data = request.data
        serializer = TodayAmountSerializer(my_model, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        my_model = TodayAmount.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class ClientViewOne(APIView):
    def get(self,request):
        user = request.user
        my_model = user.client_set.all()
        serializer = ClientSerializer(my_model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])
class OrderViewOne(APIView):
    def get(self,request):
        user = request.user
        my_client = user.client_set.all()
        client = ClientSerializer(my_client,many=True).data
        client1 = client[0]["id"]
        my_model = Order.objects.filter(client=client1)
        serializer = OrderSerializer(my_model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])
class OrderDetailsViewOne(APIView):
    def get(self,request):
        user = request.user
        client = user.client_set.all()
        client = ClientSerializer(client,many=True).data
        client1 = client[0]['id']
        my_orders = Order.objects.filter(client=client1)
        order = OrderSerializer(my_orders,many=True).data
        allOrderDetails = OrderDetailsSerializer(OrderDetails.objects.all(),many=True).data
        for orderDetails in allOrderDetails:
            orderDetails['order'] = {'id':OrderDetails.objects.get(id=orderDetails['id']).order.id}
            orderDetails['product'] = {'productName':OrderDetails.objects.get(id=orderDetails['id']).product.productName}
        for ord in order:
            order1 = ord['id']
            my_model = OrderDetails.objects.filter(order_id=order1)
            serializer = OrderDetailsSerializer(my_model,many=True)
            Response(serializer.data,status=status.HTTP_200_OK)
        return Response(allOrderDetails,status=status.HTTP_200_OK)