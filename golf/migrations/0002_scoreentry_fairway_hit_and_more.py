# Generated by Django 5.1.7 on 2025-04-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreentry',
            name='fairway_hit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scoreentry',
            name='green_in_regulation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scoreentry',
            name='putts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scoreentry',
            name='up_and_down',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scoreentry',
            name='hole_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='scoreentry',
            name='strokes',
            field=models.PositiveIntegerField(),
        ),
    ]
