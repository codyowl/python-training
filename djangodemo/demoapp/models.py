from django.db import models

class FirstModel(models.Model):
	firstname = models.CharField(max_length=200)
	email = models.EmailField()
	dob = models.DateTimeField()

	def __unicode__(self):
		return self.firstname