# Generated by Django 4.1.4 on 2022-12-20 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("logo", models.ImageField(upload_to="services/logos")),
            ],
        ),
        migrations.CreateModel(
            name="PaymentUser",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payment_date", models.DateField()),
                ("expiration_date", models.DateField()),
                (
                    "service_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="VersionPagos.service",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExpiredPayments",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "penalty_fee_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "pay_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="VersionPagos.paymentuser",
                    ),
                ),
            ],
        ),
    ]