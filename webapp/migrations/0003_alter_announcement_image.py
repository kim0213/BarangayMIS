# Generated by Django 4.2.6 on 2024-01-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_announcement_image_resident_middle_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='webapp/static/images'),
        ),
    ]
