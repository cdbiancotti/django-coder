# Generated by Django 4.0.2 on 2022-03-19 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='profesión',
            new_name='profesion',
        ),
    ]
