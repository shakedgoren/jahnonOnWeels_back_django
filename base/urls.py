from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('signin/',views.register),
    path('refresh/', TokenRefreshView.as_view()),
    path('client/add', views.ClientView.as_view()),
    path('client/display', views.ClientView.as_view()),
    path('client/update/<id>', views.ClientView.as_view()),
    path('product/add', views.ProductView.as_view()),
    path('products/display', views.ProductView.as_view()),
    path('product/update/<id>', views.ProductView.as_view()),
    path('order/add', views.OrderView.as_view()),
    path('order/display', views.OrderView.as_view()),
    path('order/update/<id>', views.OrderView.as_view()),
    path('orderdetails/add', views.OrderDetailsView.as_view()),
    path('orderdetails/display', views.OrderDetailsView.as_view()),
    path('orderdetails/update/<id>', views.OrderDetailsView.as_view()),
    path('todayamount/add', views.TodayAmountView.as_view()),
    path('todayamount/display', views.TodayAmountView.as_view()),
    path('todayamount/update/<id>', views.TodayAmountView.as_view()),
    path('client/display/one', views.ClientViewOne.as_view()),
    path('order/display/one', views.OrderViewOne.as_view()),
    path('orderdetails/display/one', views.OrderDetailsViewOne.as_view()),
   ]

