from django.urls import path
from . import api

urlpatterns = [
    path('services/', api.ServiceList.as_view(), name='service_list'),
    #path('services/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),
    path('paymentusers/', api.PaymentUserList.as_view(), name='paymentuser_list'),
    #path('paymentusers/<int:pk>/', views.PaymentUserDetail.as_view(), name='paymentuser_detail'),
    path('expiredpaymentsusers/', api.ExpiredPaymentsList.as_view(), name='expiredpayments_list'),
    
]





