from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
	course_id 	= models.IntegerField()
	name 		= models.CharField(max_length=255)
	photo 		= models.ImageField(upload_to='course')
	description = models.TextField()
	slug		= models.SlugField(blank=True, editable = False)

	def __str__(self):
		return f'{self.name} Course'

	def save(self):
		self.slug = slugify(self.name)
		super(Course, self).save()

class Step_Course(models.Model):
	step_course_id 	= models.IntegerField()
	name 			= models.CharField(max_length=255)
	description 	= models.TextField()
	course			= models.ForeignKey(Course, on_delete=models.CASCADE)
	slug			= models.SlugField(blank=True, editable = False)

	def __str__(self):
		return f'{self.name} Step Course'

	def save(self):
		self.slug = slugify(self.name)
		super(Step_Course, self).save()

class Sub_Step_Course(models.Model):
	sub_step_course_id 	= models.IntegerField()
	name            	= models.CharField(max_length=255)
	explanation 		= models.TextField()
	instruction 		= models.TextField()
	code 				= models.TextField()
	hint 				= models.TextField(default='Tidak ada petunjuk')
	in_put 				= models.CharField(max_length=1000,default="",blank=True)
	output 				= models.CharField(max_length=1000,default="",blank=True)
	step_course     	= models.ForeignKey(Step_Course, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name} Sub Step Course'

	def save(self):
		self.slug = slugify(self.name)
		super(Sub_Step_Course, self).save()

class Review(models.Model):
	user    		= models.ForeignKey(User, on_delete=models.CASCADE)
	course			= models.ForeignKey(Course, on_delete=models.CASCADE)
	description 	= models.TextField()
	score 			= models.IntegerField()

	def __str__(self):
		return f'{self.user.username} {self.course.name} Review'

	def save(self, *args, **kwargs):
		super(Review, self).save(*args, **kwargs)