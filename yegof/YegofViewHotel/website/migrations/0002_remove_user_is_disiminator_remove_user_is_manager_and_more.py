# Generated by Django 4.1.3 on 2022-12-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_disiminator',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_manager',
        ),
        migrations.AddField(
            model_name='user',
            name='Phone',
            field=models.CharField(default=1, max_length=15),
        ),
    ]
