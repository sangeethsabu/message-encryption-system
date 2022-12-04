# Generated by Django 2.2.1 on 2020-01-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citizen', '0002_reg_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('complaint', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
