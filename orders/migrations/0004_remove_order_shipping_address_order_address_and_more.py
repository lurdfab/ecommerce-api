# Generated by Django 4.2.6 on 2023-11-10 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0001_initial"),
        ("orders", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="shipping_address",
        ),
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="discount.discount",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="delivery",
            field=models.CharField(
                choices=[
                    ("free", "free"),
                    ("standard", "standard"),
                    ("express", "express"),
                ],
                default="free",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="phone_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="state",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="town",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="zipcode",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
