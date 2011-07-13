
from django import test
from django.http import HttpRequest

from mobile_detector import is_mobile, use_mobile, user_declined_mobile
from mobile_detector.context_processors import detect_mobile

class MobileUtilitiesTests(test.TestCase):

    def setUp(self):
        self.request = HttpRequest()

    def test_returns_true_when_user_agent_matches_android(self):
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.assertTrue(is_mobile(self.request))

    def test_returns_true_when_user_agent_matches_iphone(self):
        self.request.META = {'HTTP_USER_AGENT': 'iphone'}
        self.assertTrue(is_mobile(self.request))

    def test_returns_false_when_user_agent_does_not_match_lists(self):
        self.request.META = {'HTTP_USER_AGENT': 'chrome'}
        self.assertFalse(is_mobile(self.request))

    def test_returns_true_when_user_has_no_mobile_cookie(self):
        self.request.COOKIES = {'no_mobile': 'True'}
        self.assertTrue(user_declined_mobile(self.request))

    def test_returns_false_when_user_does_not_have_no_mobile_cookie(self):
        self.assertFalse(user_declined_mobile(self.request))

    def test_returns_true_when_is_mobile_and_not_user_declined_mobile(self):
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.assertEqual(True, use_mobile(self.request))

    def test_returns_false_when_not_is_mobile(self):
        self.request.META = {'HTTP_USER_AGENT': 'chrome'}
        self.assertEqual(False, use_mobile(self.request))

    def test_returns_false_when_is_mobile_and_user_declined_mobile(self):
        self.request.COOKIES = {'no_mobile': 'True'}
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.assertEqual(False, use_mobile(self.request))

class ContextProcessorTests(test.TestCase):

    def setUp(self):
        self.request = HttpRequest()

    def test_returns_dict_with_use_mobile_equals_true_when_is_mobile(self):
        self.request.META = {'HTTP_USER_AGENT': 'android'}

        context = detect_mobile(self.request)
        self.assertEqual({
            'use_mobile': True,
        }, context)

    def test_returns_dict_with_use_mobile_equals_false_when_not_mobile(self):
        self.request.META = {'HTTP_USER_AGENT': 'chrome'}

        context = detect_mobile(self.request)
        self.assertEqual({
            'use_mobile': False,
        }, context)

    def test_returns_dict_with_use_mobile_equals_false_when_no_mobile_cookie_set(self):
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.request.COOKIES = {'no_mobile': 'True'}

        context = detect_mobile(self.request)
        self.assertEqual({
            'use_mobile': False,
        }, context)