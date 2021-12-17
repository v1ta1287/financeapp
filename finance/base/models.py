from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stats(models.Model):
	salary = models.IntegerField()

class Expense(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	name = models.CharField(max_length = 20)
	amount = models.IntegerField()
	choices = (
		('GROCERIES', 'Money spent on groceries'),
		('BILLS', 'Money spent on water/electricity/internet bills'),
		('RENT', 'Money spent on rent'),
		('OTHER', 'Other weekly expenses')

	)
	category = models.CharField(max_length = 20, choices = choices, default = 'OTHER')
	importance = models.IntegerField()
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return 'Expense : {0}'.format(self.name)





