from django.conf.urls import patterns, url
from django.views.generic import (
        TemplateView,
        ListView,
        )

from models import BlogEntry
from views import BlogEntryDetailView

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=BlogEntry.objects.all_public())),
    url(r'^(?P<slug>[-_\w0-9]+)/(?P<pk>[0-9]+)/$',
        BlogEntryDetailView.as_view(), name='blogentry_detail'),
    url(r'^info/', TemplateView.as_view(template_name='blog/info.html')),
)
