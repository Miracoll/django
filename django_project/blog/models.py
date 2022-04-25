from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	name=models.TextField(max_length=191)
	price=models.TextField(max_length=50)
	description=models.TextField(max_length=500, null=True)

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date']

class Comment(models.Model):
	comment = models.TextField(max_length=5000)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.owner} comment'