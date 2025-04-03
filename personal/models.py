from django.db import models
from django.utils import timezone

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.id)
    
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    shown = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False)
    github_url = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now) 
    description = models.TextField()
    icon = models.ImageField(upload_to='icons', null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    images = models.ManyToManyField(Image, related_name='posts', blank=True)
    videos = models.ManyToManyField(Video, related_name='posts', blank=True)

    def __str__(self):
        state = "Personal"
        if self.is_main == False:
            state = "Hobby"
        return self.title + " (" + state + ")"
    
class Ability(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    description = models.TextField()
    is_coursework = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        state = "Coursework"
        if self.is_coursework == False:
            state = "Certificate"
        return self.tag + " (" + state + ")"

class Me(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.ImageField(upload_to='icons', null=True, blank=True)
    description = models.TextField()
    about_me = models.TextField()

    abilities = models.ManyToManyField(Ability, related_name='me', blank=True)

    def __str__(self):
        return str(self.id)