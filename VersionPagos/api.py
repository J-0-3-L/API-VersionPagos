from .models import Service, PaymentUser, ExpiredPayments
from .serializers import ServiceSerializer, PaymentUserSerializer, ExpiredPaymentsSerializer
from rest_framework.permissions import AllowAny, IsAdminUser ,IsAuthenticated
from rest_framework import viewsets, filters 
from .pagination import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework import status

from rest_framework.throttling import UserRateThrottle

from rest_framework import generics


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]
    http_method_names = ['get']
    #permission_classes = [IsAuthenticated]
# class CrearServicio(generics.CreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

class PaymentUserList(generics.ListCreateAPIView):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'expiration_date']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment_date = serializer.validated_data['payment_date']
        expiration_date = serializer.validated_data['expiration_date']
        if payment_date > expiration_date:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    throttle_classes = [UserRateThrottle]

# class PaymentList(generics.ListCreateAPIView):
#     queryset = PaymentUser.objects.all()
#     serializer_class = PaymentUserSerializer

class ExpiredPaymentsList(generics.ListCreateAPIView):
    queryset = ExpiredPayments.objects.all()
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post']
    # permission_classes = [IsAuthenticated]
# class ExpiredPayments(generics.ListCreateAPIView):
#     queryset = PaymentUser.objects.all()
#     serializer_class = PaymentUserSerializer
