from django.db import models

# Create your models here.
class Char(models.Model):
	name = models.CharField(max_length = 15, verbose_name = 'Character')
	description = models.TextField(verbose_name = 'Description')
	mains = models.TextField(verbose_name ="Mains")
	pref = models.TextField(verbose_name="Preferences")
	image =  models.CharField(max_length = 50)
	stripname = models.CharField(max_length = 15, verbose_name = 'stripname')

	def serialize(self):
		return {
		"name": self.name,
		"description": self.description,
		"pref": self.pref,
		"mains": self.mains,
		"image": self.image,
		"stripname": self.stripname
		}
