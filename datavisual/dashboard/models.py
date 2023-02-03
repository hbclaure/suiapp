from django.db import models

# Create your models here.
class CountryData(models.Model):
	date = models.CharField(max_length = 100)
	weight = models.IntegerField()



	class Meta:
		verbose_name_plural = 'Country Pouplation Data'

	def __str__(self):
		return f'{self.date}-{self.weight}'

class deadlifting(models.Model):
	date2 = models.CharField(max_length = 100,default='deadlifting')
	weight2 = models.IntegerField(default=120)

	class Meta:
		verbose_name_plural = 'new Pouplation Data'

	def __str__(self):
		return f'{self.date2}-{self.weight2}'


class sideshoulder(models.Model):
	date3 = models.CharField(max_length = 100,default='sideshoulder')
	weight3 = models.IntegerField(default=120)

	class Meta:
		verbose_name_plural = 'hi Pouplation Data'

	def __str__(self):
		return f'{self.date3}-{self.weight3}'


class frontshoulder(models.Model):
	date4 = models.CharField(max_length = 100,default='sideshoulder')
	weight4 = models.IntegerField(default=120)

	class Meta:
		verbose_name_plural = 'Frontshoulder Data'

	def __str__(self):
		return f'{self.date4}-{self.weight4}'



class squatting(models.Model):
	date5 = models.CharField(max_length = 100,default='sideshoulder')
	weight5= models.IntegerField(default=120)

	class Meta:
		verbose_name_plural = 'squatting Data'

	def __str__(self):
		return f'{self.date5}-{self.weight5}'


class backpull(models.Model):
	date6 = models.CharField(max_length = 100,default='sideshoulder')
	weight6 = models.IntegerField(default=120)

	class Meta:
		verbose_name_plural = 'backpull Data'

	def __str__(self):
		return f'{self.date6}-{self.weight6}'

class pullups(models.Model):
	date7 = models.CharField(max_length = 100,default='sideshoulder')
	weight7 = models.IntegerField(default=120)

	class Meta:
		verbose_name_plural = 'pullups Data'

	def __str__(self):
		return f'{self.date7}-{self.weight7}'


