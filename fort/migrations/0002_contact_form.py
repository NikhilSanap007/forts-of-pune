# Generated by Django 4.0.6 on 2022-09-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fort', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
