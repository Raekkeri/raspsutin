from django.conf.urls import patterns, url
from django.views.generic import (
        TemplateView,
        ListView,
        )

from models import BlogEntry

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=BlogEntry.objects.all_public())),
    url(r'^info/', TemplateView.as_view(template_name='blog/info.html')),
)
