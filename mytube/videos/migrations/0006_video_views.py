# Generated by Django 4.1.7 on 2023-04-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0005_alter_video_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="video", name="views", field=models.IntegerField(default=0),
        ),
    ]
