from django.db import models


class CategoryManager(models.Manager):
    pass


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category")


class JobManager(models.Manager):
    pass


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
        'Category', related_name='category', on_delete=models.CASCADE
    )
    tutor = models.ForeignKey(
        'accounts.Tutor', related_name='tutor', on_delete=models.CASCADE
    )


class ScheduleManager(models.Manager):
    pass


class Schedule(models.Model):
    day = models.DateField()
    duration = models.DurationField()


class ReviewManager(models.Manager):
    pass


class Review(models.Model):
    sender = models.ForeignKey(
        'accounts.User', related_name='sender', on_delete=models.CASCADE
    )
    recip = models.ForeignKey(
        'accounts.Tutor', related_name='recip', on_delete=models.CASCADE
    )
    quality = models.IntegerField()
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
