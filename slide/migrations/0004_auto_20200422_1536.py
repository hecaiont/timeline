# Generated by Django 3.0 on 2020-04-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0003_auto_20200422_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['title', 'start_date']},
        ),
    ]
