# Generated by Django 2.1.4 on 2019-01-02 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=30)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_name', models.CharField(max_length=30)),
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('deparment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='more_table.Deparment')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField(default=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('sd_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='more_table.Student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='more_table.Student'),
        ),
    ]
