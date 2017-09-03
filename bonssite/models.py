from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=200);

    def __str__(self):
        return self.title;

    def get_section_articles(self):
        return Article.objects.filter(section=self.id);

class Article(models.Model):
    title = models.CharField(max_length=200);
    description = models.TextField();
    #content = models.TextField();
    content = HTMLField();
    author = models.ForeignKey(User);
    section = models.ForeignKey(Section);
    creationDate = models.DateField();
    lastEditDate = models.DateField();

    def __str__(self):
        return self.title;