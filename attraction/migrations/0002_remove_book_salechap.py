# Generated by Django 3.2.8 on 2021-11-11 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='salechap',
        ),
    ]
