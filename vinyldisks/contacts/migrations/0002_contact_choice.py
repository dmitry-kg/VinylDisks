# Generated by Django 4.1.6 on 2023-03-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='choice',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
