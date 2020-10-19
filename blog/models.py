from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='images/')
	body = models.TextField()
		
	def summery(self):
		
		if len(self.body) > 100:
			return self.body[:100] + '...'
		elif len(self.body) <= 100:
			return self.body


	def pup_date_p(self):
		return self.pub_date.strftime('%b %e %Y') 

	def __str__(self):
		return self.title