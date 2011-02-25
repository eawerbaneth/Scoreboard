from django.db import models
import datetime

class Achievement(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.name
	def was_published_today(self):
		return self.pub_date.date()==datetime.date.today()
	was_published_today.short_description='Published today?'

class Gold(models.Model):
	achiev = models.ForeignKey(Achievement)
	describ = models.CharField(max_length=500)
	def __unicode__(self):
		return self.describ
class Silver(models.Model):
	achiev = models.ForeignKey(Achievement)
	describ = models.CharField(max_length=500)
	def __unicode__(self):
		return self.describ
	
class Bronze(models.Model):
	achiev = models.ForeignKey(Achievement)
	describ = models.CharField(max_length=500)
	def __unicode__(self):
		return self.describ
	

