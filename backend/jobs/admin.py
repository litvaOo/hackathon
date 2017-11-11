from django.contrib import admin
from jobs.models import Category, Job, Schedule, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
# Register your models here.
