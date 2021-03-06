# Generated by Django 3.0.5 on 2020-04-09 00:45

from django.db import migrations, models
import submission.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mailerSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('template', models.FileField(blank=True, null=True, upload_to=submission.models.upload_image_path)),
            ],
        ),
    ]
