# Generated by Django 5.0.6 on 2024-06-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0003_alter_user_telegram_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255),
        ),
    ]
