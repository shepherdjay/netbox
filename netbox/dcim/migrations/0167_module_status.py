# Generated by Django 4.1.2 on 2022-12-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0166_virtualdevicecontext'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]