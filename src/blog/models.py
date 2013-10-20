from django.db import models
from django.utils import timezone
from django_extensions.db.fields import (
        AutoSlugField,
        CreationDateTimeField,
        )


class BlogEntry(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    publish_date = models.DateTimeField()
    creation_date = CreationDateTimeField()
    is_public = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title')

    def save(self, *args, **kwargs):
        if not self.publish_date:
            self.publish_date = timezone.now()
        return super(BlogEntry, self).save(*args, **kwargs)
