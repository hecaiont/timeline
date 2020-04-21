# Generated by Django 3.0 on 2020-04-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField(blank=True, max_length=500)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('highlight', models.BooleanField(default=False)),
                ('tags', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
