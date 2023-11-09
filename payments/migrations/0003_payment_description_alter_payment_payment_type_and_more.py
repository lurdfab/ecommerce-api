# Generated by Django 4.2.6 on 2023-11-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="description",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.CharField(
                choices=[
                    ("cash", "cash_on_delivery"),
                    ("paypal", "paypal"),
                    ("cc", "credit_card"),
                    ("transfer", "Bank Transfer"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "pending"),
                    ("puccessful", "successful"),
                    ("declined", "declined"),
                ],
                default=0,
            ),
        ),
    ]
