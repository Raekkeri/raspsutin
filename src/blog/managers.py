from django.db import models


class BlogManager(models.Manager):
    def all_public(self):
        qs = self.get_query_set()
        qs = qs.filter(is_public=True)
        return qs
