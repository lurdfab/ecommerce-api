# Generated by Django 4.2.6 on 2023-11-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0006_payment_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]