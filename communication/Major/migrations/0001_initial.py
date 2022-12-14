# Generated by Django 2.2.1 on 2020-01-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('bgrp', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('dname', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('regno', models.IntegerField()),
                ('uname', models.CharField(max_length=20)),
            ],
        ),
    ]
