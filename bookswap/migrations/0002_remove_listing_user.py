# Generated by Django 3.1 on 2020-11-20 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookswap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
    ]
