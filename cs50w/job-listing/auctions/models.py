from django.contrib.auth.models import AbstractUser
from django.db import models

#internship site.

class User(AbstractUser):
    pass

class Listings(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=50)
    description = models.TextField()
    company_url = models.URLField(blank=True, null=True)
    category = models

