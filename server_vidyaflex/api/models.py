from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student = models.BooleanField(default=False)


class StudentTeacher(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField()
    email = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=250)
    profileimage = models.ImageField(upload_to="student_profile/")
    student = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    skill_name = models.CharField(max_length=255)


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField( null=True, blank=True)
    course_price = models.CharField(max_length=1000, null=True, blank=True)
    course_rating = models.CharField(max_length=255, null=True, blank=True)
    course_overview = models.TextField( null=True, blank=True)
    course_profile = models.ImageField(
        upload_to="course_profile/", null=True, blank=True
    )
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    students = models.ManyToManyField(
        StudentTeacher, related_name="enrolled_courses", null=True, blank=True
    )
    teacher = models.ForeignKey(
        StudentTeacher,
        on_delete=models.CASCADE,
        related_name="taught_courses",
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(
        Skill, related_name="courses", null=True, blank=True
    )


class CourseAssignment(models.Model):
    assignment_name = models.CharField(max_length=255)
    assignment_description = models.TextField()
    assignment_end_date = models.DateField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="assignments"
    )


class AssignmentStudent(models.Model):
    assignment_description = models.TextField()
    assignment = models.ForeignKey(
        CourseAssignment, on_delete=models.CASCADE, related_name="submitted_assignments"
    )
    student = models.ForeignKey(
        StudentTeacher, on_delete=models.CASCADE, related_name="assignments"
    )
    assignment_file = models.FileField(upload_to="assignments/")


class CourseMessage(models.Model):
    message = models.CharField(max_length=255)
    sent_time = models.DateTimeField(auto_now_add=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="messages"
    )
    sent_by = models.ForeignKey(
        StudentTeacher, on_delete=models.CASCADE, related_name="messages_sent"
    )
    important = models.BooleanField(default=False)


class CourseMaterial(models.Model):
    material_file = models.FileField(upload_to="materials/")
    material_description = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="materials"
    )
