# Generated by Django 3.2.12 on 2022-11-02 02:44

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('unit', models.CharField(choices=[('MDN', 'MDN'), ('UMNC', 'UMNC'), ('UMNP', 'UMNP'), ('UMNT', 'UMNT')], max_length=4, null=True)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('published', models.DateField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]