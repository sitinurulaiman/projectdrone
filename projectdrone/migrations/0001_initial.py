# Generated by Django 4.0.3 on 2022-03-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=25)),
                ('uname', models.CharField(max_length=40)),
                ('pwd', models.CharField(max_length=25)),
                ('pwd2', models.CharField(max_length=25)),
            ],
        ),
    ]