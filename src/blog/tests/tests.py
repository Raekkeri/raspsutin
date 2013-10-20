from djobjectfactory import get_factory, ObjectFactory

from helpers import BaseTestCase
from blog.models import BlogEntry


__all__ = ['TestManagers']


class BlogObjectFactory(ObjectFactory):
    model = 'blog.BlogEntry'
    def default(self, counter):
        return {
                'title': 'Blogentry %d' % counter,
                'text': 'Some blog text',
                }


class TestManagers(BaseTestCase):
    def test_get_public(self):
        obj1 = get_factory('blog.BlogEntry').create(is_public=True)
        obj2 = get_factory('blog.BlogEntry').create(is_public=False)
        obj3 = get_factory('blog.BlogEntry').create(is_public=True)
        qs = BlogEntry.objects.all_public()
        self.assert_ids(qs, [obj1, obj3])
