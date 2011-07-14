
from django import test
from django.core.urlresolvers import reverse
from django.http import HttpRequest

from mobile_detector import is_mobile, use_mobile, no_mobile_cookie
from mobile_detector import get_mobile_cookie_name
from mobile_detector.context_processors import detect_mobile

__all__ = (
    'MobileUtilitiesTests', 'ContextProcessorTests',
    'MobileDetectorViewTests',
)

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

    def test_returns_true_when_user_has_mobile_cookie_false(self):
        self.request.COOKIES = {get_mobile_cookie_name(): 'false'}
        self.assertTrue(no_mobile_cookie(self.request))

    def test_returns_false_when_user_has_mobile_cookie_true(self):
        self.request.COOKIES = {get_mobile_cookie_name(): 'true'}
        self.assertFalse(no_mobile_cookie(self.request))

    def test_returns_false_when_user_does_not_have_mobile_cookie(self):
        self.assertFalse(no_mobile_cookie(self.request))

    def test_returns_true_when_is_mobile_and_not_user_declined_mobile(self):
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.assertEqual(True, use_mobile(self.request))

    def test_returns_false_when_not_is_mobile(self):
        self.request.META = {'HTTP_USER_AGENT': 'chrome'}
        self.assertEqual(False, use_mobile(self.request))

    def test_returns_false_when_is_mobile_and_user_declined_mobile(self):
        self.request.COOKIES = {get_mobile_cookie_name(): 'false'}
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.assertEqual(False, use_mobile(self.request))

    def test_returns_true_when_is_not_mobile_but_has_mobile_cookie(self):
        self.request.COOKIES = {get_mobile_cookie_name(): 'true'}
        self.request.META = {'HTTP_USER_AGENT': 'chrome'}
        self.assertEqual(True, use_mobile(self.request))

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

    def test_returns_dict_with_use_mobile_equals_false_when_mobile_cookie_is_false(self):
        self.request.META = {'HTTP_USER_AGENT': 'android'}
        self.request.COOKIES = {get_mobile_cookie_name(): 'false'}

        context = detect_mobile(self.request)
        self.assertEqual({
            'use_mobile': False,
        }, context)

class MobileDetectorViewTests(test.TestCase):

    def test_force_mobile_sets_mobile_cookie_to_true_and_redirects_to_next_parameter(self):
        expected_url = 'http://www.example.com/next'
        response = self.client.get(reverse("force_mobile"), data={'next': expected_url})
        self.assertEqual(302, response.status_code)
        self.assertTrue(expected_url, response['Location'])
        self.assertEqual('Set-Cookie: use_mobile=true; Path=/', str(response.cookies))
        
    def test_force_desktop_sets_mobile_cookie_to_false_and_redirects_to_next_parameter(self):
        expected_url = 'http://www.example.com/next'
        response = self.client.get(reverse("force_desktop"), data={'next': expected_url})
        self.assertEqual(302, response.status_code)
        self.assertTrue(expected_url, response['Location'])
        self.assertEqual('Set-Cookie: use_mobile=false; Path=/', str(response.cookies))