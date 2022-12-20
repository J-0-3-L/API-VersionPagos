from django.db import models
from users.models import User

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='services/logos')

class PaymentUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    expiration_date = models.DateField()

class ExpiredPayments(models.Model):
    id = models.AutoField(primary_key=True)
    pay_user_id = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_fee_amount = models.DecimalField(max_digits=10, decimal_places=2)