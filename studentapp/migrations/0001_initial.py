# Generated by Django 4.2 on 2023-05-31 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('MobileNumber', models.BigIntegerField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.place')),
            ],
        ),
    ]
