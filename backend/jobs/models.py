from django.db import models
from accounts.models import Tutor, User


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="category/", blank=True, null=True, max_length=1000)
    parent_category = models.ForeignKey(
        'self', related_name="sub_category", blank=True, null=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    P_CHOICES = (
        (0, 'Hour'),
        (1, 'Day'),
        (2, 'Week'),
        (3, 'Month'),
        (4, 'Course'),
    )
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    price_per = models.SmallIntegerField(choices=P_CHOICES)
    category = models.ForeignKey(
        Category, related_name='jobs')
    tutor = models.ForeignKey(
        Tutor, related_name='jobs')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    day = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return self.day


class Review(models.Model):
    sender = models.ForeignKey(
        User, related_name='reviews'
    )
    recipient = models.ForeignKey(
        Tutor, related_name='reviews'
    )
    quality = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    job = models.ForeignKey(
        'Job', related_name='reviews', blank=True, null=True
    )

    def __str__(self):
        return self.description


class Booking(models.Model):
    day = models.DateField()
    duration = models.DurationField()
    job = models.ForeignKey(
        Job, related_name='bookings'
    )
    sender = models.ForeignKey(
        User, related_name='bookings'
    )

    def __str__(self):
        return self.job.title
