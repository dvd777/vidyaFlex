from django.contrib import admin
from .models import (
    StudentTeacher,
    User,
    Course,
    Skill,
    CourseMessage,
    CourseAssignment,
    AssignmentStudent,
    CourseMaterial,
)

# Register your models here.
admin.site.register(StudentTeacher)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(CourseAssignment)
admin.site.register(AssignmentStudent)
admin.site.register(CourseMaterial)


class CourseMessageAdmin(admin.ModelAdmin):
    list_display = ("message", "sent_time", "course", "sent_by", "important")
    readonly_fields = ("sent_time",)

    fieldsets = (
        (None, {"fields": ("message", "sent_time", "course", "sent_by", "important")}),
    )


admin.site.register(CourseMessage, CourseMessageAdmin)
