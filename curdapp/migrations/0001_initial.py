# Generated by Django 2.1 on 2019-06-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('roll_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=4)),
            ],
        ),
    ]