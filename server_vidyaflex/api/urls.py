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
    path("coursemessages/<int:pk>/", CourseMessageAPIView.as_view()),
    path("coursematerials/", CourseMaterialAPIView.as_view()),
    path("coursematerials/<int:pk>/", CourseMaterialAPIView.as_view()),
]
