# Generated by Django 5.0.7 on 2024-08-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_user_teacher_alter_course_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_price',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
