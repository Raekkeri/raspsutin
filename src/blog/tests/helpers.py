from django.test import TestCase


__all__ = ['BaseWithUtils', 'BaseTestCase']


class BaseWithUtils(object):
    def assert_ids(self, li, expected):
        g = zip(li, expected)
        for i1, i2 in g:
            self.assertEquals(i1.id, i2.id)


class BaseTestCase(BaseWithUtils, TestCase):
    pass
