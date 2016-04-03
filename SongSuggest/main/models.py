from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
# 	name = models.CharField(max_length = 50)
# 	password = models.CharField(max_length = 10)
# 	admin = models.BooleanField()

# 	def __str__(self):
# 		return str(self.id)

class Suggestion(models.Model):
	voters = models.ManyToManyField(User, related_name='voters', through='Vote')
	title = models.CharField(max_length = 100)
	artist = models.CharField(max_length = 100)
	category = models.CharField(max_length = 20)
	commentary = models.TextField()
	points = models.IntegerField()
	owner = models.ForeignKey(User, related_name='owner')

	def __str__(self):
		return str(self.id)

class Vote(models.Model):
	voter = models.ForeignKey(User)
	suggestion = models.ForeignKey(Suggestion)
	vote = models.BooleanField() #0 for negative, 1 for positive

	def __str__(self):
		return '%s %s' % (self.id, self.customerOrder)