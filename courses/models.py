from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')

class Categories(models.Model):
   name = models.CharField(max_length=100 ,null=False, unique=True)

   def __str__(self):
       return self.name

class ItemsBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(null=False, max_length=255)
    image = models.ImageField(upload_to='courses/%Y/%m',default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Course(ItemsBase):
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ["-id"]
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)

class lesson(ItemsBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)