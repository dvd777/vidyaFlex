from django.urls import path
from .views import (
    StudentAPIView,
    TeacherAPIView,
    SkillAPIView,
    CourseAPIView,
    CourseAssignmentAPIView,
    AssignmentStudentAPIView,
    CourseMessageAPIView,
    CourseMaterialAPIView,
    RegisterView,
    LoginView,
)
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("student/", StudentAPIView.as_view()),
    path("student/<int:pk>/", StudentAPIView.as_view()),
    path("teacher/", TeacherAPIView.as_view()),
    path("teacher/<int:pk>/", TeacherAPIView.as_view()),
    path("skills/", SkillAPIView.as_view()),
    path("skills/<int:pk>/", SkillAPIView.as_view()),
    path("courses/", CourseAPIView.as_view()),
    path("courses/<int:pk>/", CourseAPIView.as_view()),
    path("courseassignments/", CourseAssignmentAPIView.as_view()),
    path("courseassignments/<int:pk>/", CourseAssignmentAPIView.as_view()),
    path("assignmentstudents/", AssignmentStudentAPIView.as_view()),
    path("assignmentstudents/<int:pk>/", AssignmentStudentAPIView.as_view()),
    path("coursemessages/", CourseMessageAPIView.as_view()),
    path("coursemessages/<int:course_id>/", CourseMessageAPIView.as_view()),
    path("coursematerials/", CourseMaterialAPIView.as_view()),
    path("coursematerials/<int:pk>/", CourseMaterialAPIView.as_view()),
    path("enroll/<int:course_id>/", update_course_students, name="enroll"),
    path(
        "student/<int:student_teacher_id>/assignments/",
        student_assignments,
        name="student-assignments",
    ),
    path(
        "assignments/<int:assignment_id>/files/",
        assignment_student_files,
        name="assignment-student-files",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
