# Generated by Django 4.2 on 2023-05-31 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_rename_place_student_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place',
            new_name='city',
        ),
    ]