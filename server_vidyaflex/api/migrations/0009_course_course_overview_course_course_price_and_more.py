# Generated by Django 5.0.7 on 2024-08-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_skills_skill_remove_course_skill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_overview',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_profile',
            field=models.ImageField(blank=True, null=True, upload_to='course_profile/'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_rating',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
