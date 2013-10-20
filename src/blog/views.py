from django.views.generic import DetailView
from models import BlogEntry


class BlogEntryDetailView(DetailView):
    queryset = BlogEntry.objects.all_public()

    def get_object(self, queryset=None):
        # Override get_object so that slug is forced to match
        qs = self.get_queryset()
        qs = qs.filter(slug=self.kwargs['slug'])
        return super(BlogEntryDetailView, self).get_object(qs)
