# Generated by Django 2.2.1 on 2020-01-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citizen', '0003_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('rtype', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
