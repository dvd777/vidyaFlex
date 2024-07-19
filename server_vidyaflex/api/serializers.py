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
    class Meta:
        model = StudentTeacher
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAssignment
        fields = "__all__"


class AssignmentStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentStudent
        fields = "__all__"


class CourseMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMessage
        fields = "__all__"


class CourseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
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
