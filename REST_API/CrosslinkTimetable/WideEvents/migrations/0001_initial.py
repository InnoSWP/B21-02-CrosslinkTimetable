# Generated by Django 4.0.5 on 2022-06-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('time_from', models.DateTimeField(auto_now=True)),
                ('time_to', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
