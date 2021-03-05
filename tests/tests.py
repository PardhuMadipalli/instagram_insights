import unittest
from unittest.mock import patch
import requests_mock
import os
import sys

from insights import timings
from insights import hashtags

from instagram import restmethods
from instagram import instagram_data

import get_insta_insights

tests_dir = os.path.dirname(os.path.realpath(__file__)) + "/"


class TestInsights(unittest.TestCase):

    def test_timings(self):
        timings.get_timing_insights(tests_dir + "sample_insights.csv", 2)

    def test_hashtags(self):
        hashtags.get_best_tags(tests_dir + "sample_insights.csv", True, 3)


class TestInstagram(unittest.TestCase):
    def test_missing_token(self):
        self.assertRaises(Exception, instagram_data.get_insights, None, '123')


class TestMain(unittest.TestCase):

    def test_sys_argv_help(self):
        with patch.object(sys, "argv", ["get_insta_insights.py", "--help"]):
            with self.assertRaises(SystemExit):
                get_insta_insights.main()

    def test_sys_argv_ml(self):
        with patch.object(sys, "argv", ["get_insta_insights.py", "-m"]):
            self.assertRaises(RuntimeError, get_insta_insights.main)

    def test_sys_argv_page(self):
        with patch.object(sys, "argv", ["get_insta_insights.py", "--page-id", "123"]):
            self.assertRaises(Exception, get_insta_insights.main)

    def test_sys_argv_token(self):
        with patch.object(sys, "argv", ["get_insta_insights.py", "--token", "token"]):
            self.assertRaises(Exception, get_insta_insights.main)

    def test_sys_argv_num_timing_tags(self):
        with patch.object(sys, "argv", ["get_insta_insights.py", "--token",
                                        "token", "--page-id", "123", "--num-timings", "2", "--num-tags", "2"]):

            with open(tests_dir + "sample_posts_response.json", "r") as fileout:
                mock_posts_response = fileout.read()
            with open(tests_dir + "insights_response_101.json", "r") as fileout:
                insights_response_101 = fileout.read()
            with open(tests_dir + "response_101.json", "r") as fileout:
                response_101 = fileout.read()
            with open(tests_dir + "insights_response_202.json", "r") as fileout:
                insights_response_202 = fileout.read()
            with open(tests_dir + "response_202.json", "r") as fileout:
                response_202 = fileout.read()

            with requests_mock.Mocker() as m:
                m.register_uri('GET', '/v10.0/123/media/', text=mock_posts_response)
                m.register_uri('GET', '/v10.0/101/', text=response_101)
                m.register_uri('GET', '/v10.0/101/insights/', text=insights_response_101)
                m.register_uri('GET', '/v10.0/202/', text=response_202)
                m.register_uri('GET', '/v10.0/202/insights/', text=insights_response_202)
                get_insta_insights.main()


class TestRest(unittest.TestCase):
    def test_unreachable_get_url(self):
        self.assertRaises(Exception, restmethods.get, ['dummy'], 'token')


if __name__ == '__main__':
    unittest.main()
