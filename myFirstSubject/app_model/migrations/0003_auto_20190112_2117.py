# Generated by Django 2.1.4 on 2019-01-12 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0002_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
