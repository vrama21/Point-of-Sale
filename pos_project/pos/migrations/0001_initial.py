# Generated by Django 2.1.7 on 2019-03-10 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address_1', models.CharField(max_length=30)),
                ('address_2', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=20)),
                ('business_name', models.CharField(max_length=30)),
                ('ext', models.CharField(max_length=15)),
                ('room', models.CharField(max_length=10)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
