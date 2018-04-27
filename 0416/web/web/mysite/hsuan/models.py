from django.db import models

# Create your models here.
class People(models.Model):
	name = models.CharField(max_length=20)
	is_male = models.BooleanField(default=False)
	birth_date = models.DateField(max_length=50)
	phone_number = models.CharField(max_length=15)
	def __str__(self):
		return self.name

