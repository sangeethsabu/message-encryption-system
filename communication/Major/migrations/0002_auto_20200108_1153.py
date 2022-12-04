# Generated by Django 2.2.1 on 2020-01-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Major', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcode', models.CharField(max_length=20)),
                ('offid', models.IntegerField()),
                ('mid', models.IntegerField()),
                ('oid', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='officer',
            name='photo',
            field=models.FileField(max_length=20, upload_to='file'),
        ),
    ]
