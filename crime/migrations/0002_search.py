# Generated by Django 5.0.4 on 2024-04-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
