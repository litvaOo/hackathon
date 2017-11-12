from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category", blank=True, null=True)
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
        'Category', related_name='category', on_delete=models.CASCADE)
    tutor = models.ForeignKey(
        'accounts.Tutor', related_name='jobs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    day = models.DateField()
    duration = models.DurationField()


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
