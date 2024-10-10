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
    CourseMessageSerializerPost,
    AssignmentStudentSerializerGet,
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
                    "user_id": user.id,
                    # "teacherstudentid": studentteacher.id,
                    "role": user.student,
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
            studentteacher = StudentTeacher.objects.get(user=user)
            return Response(
                {
                    "user_id": user.id,
                    "teacherstudentid": studentteacher.id,
                    "role": user.student,
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
        tuserid = request.GET.get("tuserid", None)
        suserid = request.GET.get("suserid", None)
        if pk:
            courses = Course.objects.get(id=pk)
            serializer = CourseSerializer(courses)
            return Response(serializer.data)
        elif tuserid:
            courses = Course.objects.filter(teacher=tuserid)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        elif suserid:
            courses = Course.objects.filter(students__id=suserid)
            serializer = CourseSerializer(courses, many=True)
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
        tuserid = request.GET.get("tuserid", None)
        suserid = request.GET.get("suserid", None)

        if tuserid:
            course_assignments = CourseAssignment.objects.filter(
                course__teacher__id=tuserid
            )
        elif suserid:
            course_assignments = CourseAssignment.objects.filter(
                course__students__id=suserid
            )
        else:
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
    def get(self, request, course_id=None):
        if course_id:
            course_messages = CourseMessage.objects.filter(course_id=course_id)
        else:
            course_messages = CourseMessage.objects.all()

        serializer = CourseMessageSerializer(course_messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseMessageSerializerPost(data=request.data)
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


from rest_framework.decorators import api_view


@api_view(["POST"])
def update_course_students(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response(
            {"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND
        )

    id = request.GET.get("students")

    # if not isinstance(students_ids, list):
    #     return Response(
    #         {"error": "Students should be provided as a list."},
    #         status=status.HTTP_400_BAD_REQUEST,
    #     )

    # user= User.objects.get(id=id)

    students_to_add = StudentTeacher.objects.get(id=id)

    # if not students_to_add.exists():
    #     return Response(
    #         {"error": "No valid students found."},
    #         status=status.HTTP_400_BAD_REQUEST,
    #     )

    course.students.add(students_to_add)
    course.save()

    return Response(
        {"message": "Students added successfully."}, status=status.HTTP_200_OK
    )


@api_view(["GET"])
def student_assignments(request, student_teacher_id):
    try:
        student_teacher = StudentTeacher.objects.get(id=student_teacher_id)

        enrolled_courses = Course.objects.filter(students=student_teacher)

        assignments = CourseAssignment.objects.filter(course__in=enrolled_courses)

        serializer = CourseAssignmentSerializer(assignments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except StudentTeacher.DoesNotExist:
        return Response(
            {"error": "StudentTeacher not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def assignment_student_files(request, assignment_id):
    try:
        # Filter AssignmentStudent objects by the assignment_id
        submitted_assignments = AssignmentStudent.objects.filter(
            assignment_id=assignment_id
        )

        # Serialize the filtered objects
        serializer = AssignmentStudentSerializerGet(submitted_assignments, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

    except AssignmentStudent.DoesNotExist:
        return Response(
            {"detail": "Assignments not found."}, status=status.HTTP_404_NOT_FOUND
        )
