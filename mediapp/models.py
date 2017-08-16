from django.db import models
from django.utils import timezone

# Create your models here.
class Photo(models.Model):
	image = models.FileField(null=True, blank=True)
	caption = models.CharField(max_length=20, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	#what we return in the admin
	def __str__(self):
		return self.caption

class Video(models.Model):
	video = models.FileField(null=True, blank=True)
	caption = models.CharField(max_length=250, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	#what we return in the admin
	def __str__(self):
		return self.caption