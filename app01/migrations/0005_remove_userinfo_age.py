# Generated by Django 5.0.2 on 2024-02-21 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_delete_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='age',
        ),
    ]