# Generated by Django 2.0.3 on 2018-03-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='calendar_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]