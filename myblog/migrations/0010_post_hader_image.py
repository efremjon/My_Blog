# Generated by Django 3.2.9 on 2022-04-28 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hader_image',
            field=models.ImageField(blank=True, null=True, upload_to='Image/'),
        ),
    ]
