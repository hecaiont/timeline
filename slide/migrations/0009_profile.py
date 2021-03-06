# Generated by Django 3.0.6 on 2020-06-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0008_auto_20200507_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Man'), ('W', 'Woman'), ('O', 'Other'), ('U', 'Unknown')], max_length=2)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
    ]
