# Generated by Django 2.2.11 on 2020-03-24 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200325_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagefun',
            new_name='image',
        ),
    ]
