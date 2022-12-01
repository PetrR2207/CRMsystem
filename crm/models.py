from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crm/images/')
    url = models.URLField(blank=True)