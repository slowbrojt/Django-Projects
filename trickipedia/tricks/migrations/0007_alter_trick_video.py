# Generated by Django 4.1 on 2023-03-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0006_trick_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trick',
            name='video',
            field=models.TextField(unique=True, verbose_name='youtube embed code'),
        ),
    ]
