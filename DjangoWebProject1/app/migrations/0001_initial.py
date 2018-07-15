# Generated by Django 2.0.5 on 2018-07-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=150, verbose_name='用户名')),
                ('gender', models.CharField(default='保密', max_length=2, verbose_name='性别')),
            ],
        ),
    ]