# Generated by Django 2.2 on 2019-04-09 15:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20190409_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]