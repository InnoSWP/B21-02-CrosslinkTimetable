# Generated by Django 4.0.5 on 2022-06-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WideEvents', '0003_event_remind_before'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default=str, max_length=255),
            preserve_default=False,
        ),
    ]
