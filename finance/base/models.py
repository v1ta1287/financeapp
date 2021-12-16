from django.db import models

# Create your models here.
class Stats(models.Model):
	salary = models.IntegerField()

class Expense(models.Model):
	amount = models.IntegerField()
	category = models.CharField(max_length = 20)
	

class Task(models.Model):
	name = models.CharField(max_length = 100, blank = False)
	description = models.TextField()

	choices = (
		('DONE', 'Task has been completed'),
		('IN-PROGRESS', 'Task still needs to be completed'),
		('NOT STARTED', 'Task has not been started')
	)

	priority = models.IntegerField()
	status = models.CharField(max_length = 20, choices = choices, default = 'NOT STARTED')

	def __str__(self):
		return 'Task : {0}'.format(self.name)

