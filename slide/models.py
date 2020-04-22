from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(max_length=500, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    highlight = models.BooleanField(default=False)
    tags = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['title', 'start_date']

    def __str__(self): # show on admin change list
        return self.title

