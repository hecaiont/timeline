# Generated by Django 3.0 on 2020-05-07 07:45

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('slide', '0006_auto_20200507_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='tags',
        ),
        migrations.AddField(
            model_name='achievement',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
