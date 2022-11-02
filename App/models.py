from enum import unique
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

UNIT = (
    ('MDN', 'MDN'),
    ('UMNC', 'UMNC'),
    ('UMNP', 'UMNP'),
    ('UMNT', 'UMNT'),
)

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    unit = models.CharField(max_length=4, null=True, choices=UNIT)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    published = models.DateField(blank=True, null=True, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    @property
    def created_date(self):
        return '%s - present' % self.published.strftime('%m/%d/%Y')