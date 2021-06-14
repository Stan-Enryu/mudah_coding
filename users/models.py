from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from Browse_Course.models import Sub_Step_Course, Step_Course
# from django.utils import timezone
import datetime

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    nama            = models.CharField(max_length=255,blank=True)
    handphone       = models.CharField(max_length=15,null=True,blank=True)
    description     = models.TextField(null=True,blank=True)
    image           = models.ImageField(default='default.jpg', upload_to='profile_pics')
    time_created    = models.DateTimeField(auto_now_add=True)
    email           = models.EmailField(null=True,blank=True)
    linkedin        = models.CharField(max_length=255,null=True,blank=True)
    twitter         = models.CharField(max_length=255,null=True,blank=True)
    instagram       = models.CharField(max_length=255,null=True,blank=True)
    facebook        = models.CharField(max_length=255,null=True,blank=True)
    date_premium    = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Sub_Step_Done(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_step_course     = models.ForeignKey(Sub_Step_Course, on_delete=models.CASCADE)
    step_course         = models.ForeignKey(Step_Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.sub_step_course.name} Sub Step Done'

    def save(self, *args, **kwargs):
        super(Sub_Step_Done, self).save(*args, **kwargs)


