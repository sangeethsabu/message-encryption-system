# Generated by Django 2.2.1 on 2020-01-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Major', '0003_majortextmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='majortextmsg',
            name='encmsg',
            field=models.TextField(default=''),
        ),
    ]
