# Generated by Django 2.2.15 on 2020-11-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rest_framework_tracking", "0010_auto_20200609_1404"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apirequestlog",
            name="status_code",
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]