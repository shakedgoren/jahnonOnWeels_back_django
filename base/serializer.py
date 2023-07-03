from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Client,Product,Order,OrderDetails,TodayAmount

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    def create(self, validated_data):
        return Client.objects.create(**validated_data)  
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def create(self, validated_data):
        return Product.objects.create(**validated_data)    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'
    def create(self, validated_data):
        return OrderDetails.objects.create(**validated_data)
    
class TodayAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayAmount
        fields = '__all__'
    def create(self, validated_data):
        return TodayAmount.objects.create(**validated_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   @classmethod
   def get_token(cls, user):
       token = super().get_token(user)
       token['username'] = user.username
       token['email'] = user.email

       return token