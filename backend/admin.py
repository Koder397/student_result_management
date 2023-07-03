from django.contrib import admin

from backend.models import Student, MarkList


class MarkListInline(admin.TabularInline):
    model = MarkList


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'roll_number', 'dob')

    inlines = [
        MarkListInline
    ]


admin.site.register(Student, StudentAdmin)
