from django.db import models
from django.utils import timezone


class BlogEntry(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    publish_date = models.DateTimeField()
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.publish_date:
            self.publish_date = timezone.now()
        return super(BlogEntry, self).save(*args, **kwargs)
