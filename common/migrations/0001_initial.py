# Generated by Django 3.1.7 on 2021-03-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('stu_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('people', models.IntegerField()),
                ('income', models.FloatField()),
                ('special', models.CharField(max_length=200)),
            ],
        ),
    ]