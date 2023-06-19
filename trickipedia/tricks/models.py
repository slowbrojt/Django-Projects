from django.db import models

class Trick(models.Model):
		name = models.CharField(max_length=30, verbose_name='trick Name')
		email = models.CharField(max_length=40, verbose_name ='email')
		skier = models.CharField(max_length=30, verbose_name='skier')
		filmer = models.CharField(max_length=30, verbose_name='filmer')
		insta = models.CharField(max_length=30, blank=True, verbose_name='instagram handle')
		ns = models.CharField(max_length=30, blank=True, verbose_name='newschoolers username')
		video = models.TextField(verbose_name='youtube embed code')
		description = models.TextField()
		difficulty = models.CharField(max_length=12, blank=True)
		accepted = models.BooleanField(default = False)

# Create your models here.
