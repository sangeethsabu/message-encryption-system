# Generated by Django 2.2.1 on 2020-01-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20200108_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=250)),
                ('odate', models.CharField(max_length=20)),
                ('rname', models.CharField(max_length=20)),
                ('rtotal', models.IntegerField()),
                ('gname', models.CharField(max_length=20)),
                ('gtotal', models.IntegerField()),
                ('cname', models.CharField(max_length=20)),
                ('ctotal', models.IntegerField()),
                ('lname', models.CharField(max_length=20)),
                ('ltotal', models.IntegerField()),
            ],
        ),
    ]
