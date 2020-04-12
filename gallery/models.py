from django.db import models


# Create your models here.

class Developer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dev/img', null=True, blank=True)
    github = models.URLField()
    linkedIn = models.URLField()


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Projects(models.Model):
    name = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='projects/img', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')
    link = models.URLField()
    disc = models.TextField()
