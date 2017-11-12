from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=255, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    city = models.CharField(
        'City', max_length=50, blank=True, null=True
    )
    country = models.CharField(
        'Country', max_length=50, blank=True, null=True
    )
    birthday = models.DateField(
        'Birthday', help_text='YYYY-MM-DD',
        null=True, blank=True
    )
    avatar = models.ImageField(
        verbose_name='Avatar',
        blank=True,
        null=True,
        upload_to='avatars/',
        max_length=1000
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_full_name()


class Achievments(models.Model):
    text = models.TextField()
    organization = models.CharField(max_length=255)
    scan_file = models.FileField(
        upload_to='achievments/', blank=True, null=True)
    owner = models.ForeignKey(
        User, related_name='achievments'
    )
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Tutor(models.Model):
    user = models.ForeignKey(
        User, related_name='tutors'
    )
    about = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name
