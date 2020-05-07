from django.db import models

from taggit.managers import TaggableManager


class Achievement(models.Model):
    title = models.CharField(max_length=100)

    category_choice = (
        ('PR', 'Profile'),
		('ED', 'Education'),
        ('EX', 'Experience'),
        ('WE', 'Work Experience'),
        ('WH', 'Work History'),
        ('PS', 'Personal Summary'),
        ('SU', 'Summary'),
        ('LA', 'Language'),
        ('OB', 'Objective'),
        ('SK', 'Skills'),
        ('KS', 'Key Skills'),
        ('AD', 'Additional Infomation'),
    )
    category = models.CharField(max_length=2, choices=category_choice)
    contents = models.TextField(max_length=500, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    highlight = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self): # show on admin change list
        return self.title

