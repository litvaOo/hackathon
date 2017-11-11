from django.contrib import admin
from accounts.models import User, Tutor, Achievments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ["username"]


@admin.register(Achievments)
class AchievmentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    pass
