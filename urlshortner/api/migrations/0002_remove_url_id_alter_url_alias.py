# Generated by Django 5.0.1 on 2024-01-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='id',
        ),
        migrations.AlterField(
            model_name='url',
            name='alias',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
