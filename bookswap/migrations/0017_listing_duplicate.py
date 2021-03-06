# Generated by Django 3.1 on 2020-11-28 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookswap', '0016_listing_check_req'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing_duplicate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('have', models.CharField(max_length=120)),
                ('want', models.CharField(max_length=120)),
                ('img', models.ImageField(null=True, upload_to="images/'")),
                ('check_req', models.IntegerField(default=0, max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
