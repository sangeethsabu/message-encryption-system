# Generated by Django 2.2.1 on 2020-01-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Major', '0002_auto_20200108_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='majortextmsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('oid', models.IntegerField()),
                ('msg', models.TextField()),
                ('private', models.CharField(max_length=50)),
                ('public', models.CharField(max_length=50)),
            ],
        ),
    ]
