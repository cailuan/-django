# Generated by Django 2.1.4 on 2018-12-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('app_name', models.CharField(max_length=20)),
                ('app_number', models.IntegerField()),
            ],
        ),
    ]
