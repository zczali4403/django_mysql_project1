# Generated by Django 5.0.2 on 2024-02-21 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_department_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
    ]