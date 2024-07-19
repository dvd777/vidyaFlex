from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    User,
    StudentTeacher,
    Skill,
    Course,
    CourseAssignment,
    AssignmentStudent,
    CourseMessage,
    CourseMaterial,
)
from .serializers import (
    UserSerializer,
    StudentTeacherSerializer,
    SkillSerializer,
    CourseSerializer,
    CourseAssignmentSerializer,
    AssignmentStudentSerializer,
    CourseMessageSerializer,
    CourseMaterialSerializer,
    RegisterSerializer,
    LoginSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            student_teacher = StudentTeacher.objects.get(id=pk)
            serializer = StudentTeacherSerializer(student_teacher)
            return Response(serializer.data)
        else:
            student_teachers = StudentTeacher.objects.filter(student=True)
            serializer = StudentTeacherSerializer(student_teachers, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        student_teacher = get_object_or_404(StudentTeacher, pk=pk)
        serializer = StudentTeacherSerializer(student_teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student_teacher = get_object_or_404(StudentTeacher, pk=pk)
        student_teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            student_teacher = StudentTeacher.objects.get(id=pk)
            serializer = StudentTeacherSerializer(student_teacher)
            return Response(serializer.data)
        else:
            student_teachers = StudentTeacher.objects.filter(student=False)
            serializer = StudentTeacherSerializer(student_teachers, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        student_teacher = get_object_or_404(StudentTeacher, pk=pk)
        serializer = StudentTeacherSerializer(student_teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student_teacher = get_object_or_404(StudentTeacher, pk=pk)
        student_teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            courses = Course.objects.get(id=pk)
            serializer = CourseSerializer(courses)
            return Response(serializer.data)
        else:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseAssignmentAPIView(APIView):
    def get(self, request):
        course_assignments = CourseAssignment.objects.all()
        serializer = CourseAssignmentSerializer(course_assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course_assignment = get_object_or_404(CourseAssignment, pk=pk)
        serializer = CourseAssignmentSerializer(course_assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course_assignment = get_object_or_404(CourseAssignment, pk=pk)
        course_assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignmentStudentAPIView(APIView):
    def get(self, request):
        assignment_students = AssignmentStudent.objects.all()
        serializer = AssignmentStudentSerializer(assignment_students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        assignment_student = get_object_or_404(AssignmentStudent, pk=pk)
        serializer = AssignmentStudentSerializer(assignment_student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        assignment_student = get_object_or_404(AssignmentStudent, pk=pk)
        assignment_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseMessageAPIView(APIView):
    def get(self, request):
        course_messages = CourseMessage.objects.all()
        serializer = CourseMessageSerializer(course_messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course_message = get_object_or_404(CourseMessage, pk=pk)
        serializer = CourseMessageSerializer(course_message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course_message = get_object_or_404(CourseMessage, pk=pk)
        course_message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseMaterialAPIView(APIView):
    def get(self, request):
        course_materials = CourseMaterial.objects.all()
        serializer = CourseMaterialSerializer(course_materials, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course_material = get_object_or_404(CourseMaterial, pk=pk)
        serializer = CourseMaterialSerializer(course_material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course_material = get_object_or_404(CourseMaterial, pk=pk)
        course_material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
