from rest_framework import serializers
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
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class StudentTeacherSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        student_teacher = attrs.get("student")
        userid = attrs.get("user")

        # try:
        #     user = User.objects.get(id=userid)
        # except User.DoesNotExist:
        #     raise serializers.ValidationError("User does not exist.")

        if student_teacher:
            userid.student = True
        else:
            userid.student = False

        userid.save()
        return attrs

    class Meta:
        model = StudentTeacher
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"



class CourseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = "__all__"

        
class CourseSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, required=False)
    students = StudentTeacherSerializer(many=True, required=False)
    materials = CourseMaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            "id",
            "course_name",
            "course_description",
            "course_price",
            "course_rating",
            "course_overview",
            "course_profile",
            "course_start_date",
            "course_end_date",
            "students",
            "teacher",
            "skills",
            "materials"
        ]

    def validate_course_price(self, value):
        # Add custom validation for price if needed
        return value

    def validate_course_rating(self, value):
        # Add custom validation for rating if needed
        return value


class CourseAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAssignment
        fields = "__all__"


class AssignmentStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentStudent
        fields = "__all__"


class AssignmentStudentSerializerGet(serializers.ModelSerializer):
    student = StudentTeacherSerializer()

    class Meta:
        model = AssignmentStudent
        fields = "__all__"


class CourseMessageSerializer(serializers.ModelSerializer):
    sent_by = StudentTeacherSerializer()

    class Meta:
        model = CourseMessage
        fields = "__all__"


class CourseMessageSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = CourseMessage
        fields = "__all__"





class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
