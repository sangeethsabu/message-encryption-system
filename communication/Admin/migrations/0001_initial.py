# Generated by Django 2.2.1 on 2020-01-08 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('pwd', models.BigIntegerField()),
                ('utype', models.CharField(max_length=10)),
            ],
        ),
    ]
