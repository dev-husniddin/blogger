# Generated by Django 4.2.4 on 2023-09-03 13:18

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='posts/images'),
        ),
    ]
