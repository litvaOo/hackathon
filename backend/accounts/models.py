from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AchievmentsManager(models.Manager):
    pass


class Achievments(models.Model):
    text = models.TextField()
    organization = models.CharField(max_length=255)
    scan_file = models.FileField()
    owner = models.ForeignKey('User', related_name='achievments', on_delete=models.CASCADE)


class TutorManager(models.Manager):
    pass


class Tutor(models.Model):
    user = models.ForeignKey('User', related_name='tutor', on_delete=models.CASCADE)
    about = models.CharField(max_length=150)
    desc = models.CharField(max_length=500)


class UserManager(BaseUserManager):
    pass


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255, null=True, unique=True, default=None)
    first_name = models.CharField(max_length=255, blank=False, default='')
    last_name = models.CharField(max_length=255, blank=False, default='')
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_of_birth = models.DateField(
        null=True, default=None, help_text='YYYY-MM-DD')
    avatar = models.ImageField(
        verbose_name='profile image',
        max_length=255,
        blank=True,
        upload_to='user/profile_image/%Y')
    is_admin = models.BooleanField(default=False, verbose_name='admin')
    is_superuser = models.BooleanField(default=False, verbose_name='superuser')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()            

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'