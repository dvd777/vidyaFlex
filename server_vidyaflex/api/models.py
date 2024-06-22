from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student = models.BooleanField(default=False)
    teacher = models.BooleanField(default=False)


class StudentTeacher(models.Model):  # Renamed to follow consistent naming conventions
    name = models.CharField(max_length=250, null=True, blank=True)
    bio = models.CharField(max_length=255)
    email = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=250)
    profileimage = models.ImageField(upload_to="student_profile/")
    student = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    skill_name = models.CharField(max_length=255)


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.CharField(max_length=255)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    students = models.ManyToManyField(StudentTeacher, related_name="enrolled_courses")
    teacher = models.ForeignKey(
        StudentTeacher, on_delete=models.CASCADE, related_name="taught_courses"
    )
    skills = models.ManyToManyField(Skill, related_name="courses")


class CourseAssignment(models.Model):
    assignment_name = models.CharField(max_length=255)
    assignment_description = models.CharField(max_length=255)
    assignment_end_date = models.DateField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="assignments"
    )


class AssignmentStudent(models.Model):
    assignment_description = models.CharField(max_length=255)
    assignment = models.ForeignKey(
        CourseAssignment, on_delete=models.CASCADE, related_name="submitted_assignments"
    )
    student = models.ForeignKey(
        StudentTeacher, on_delete=models.CASCADE, related_name="assignments"
    )
    assignment_file = models.FileField(upload_to="assignments/")  # Fixed typo


class CourseMessage(models.Model):
    message = models.CharField(max_length=255)
    sent_time = models.DateTimeField(auto_now_add=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="messages"
    )  # Changed related_name
    sent_by = models.ForeignKey(
        StudentTeacher, on_delete=models.CASCADE, related_name="messages_sent"
    )
    important = models.BooleanField(default=False)


class CourseMaterial(models.Model):  # Renamed to follow singular convention
    material_file = models.FileField(upload_to="materials/")
    material_description = models.CharField(max_length=255)  # Renamed for consistency
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="materials"
    )  # Added course relation
