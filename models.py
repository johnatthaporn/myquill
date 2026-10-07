from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    properties = QuillField()

    def __str__(self):
        return self.name