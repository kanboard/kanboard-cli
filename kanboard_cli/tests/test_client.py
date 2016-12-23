# The MIT License (MIT)
#
# Copyright (c) 2016 Frederic Guillot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import kanboard
import mock
import os
import unittest

from kanboard_cli import client
from kanboard_cli import exceptions


class TestClientManager(unittest.TestCase):

    def setUp(self):
        os.environ = dict()
        self.options = mock.Mock(url=None, username=None, password=None, auth_header=None)
        self.client = client.ClientManager(self.options)

    def test_get_url_not_defined(self):
        with self.assertRaises(exceptions.KanboardException):
            self.client.get_url()

    def test_get_url_defined_with_option(self):
        self.options.url = 'some url'
        self.assertEqual('some url', self.client.get_url())

    def test_get_url_defined_with_env_variable(self):
        os.environ['KANBOARD_URL'] = 'another url'
        self.assertEqual('another url', self.client.get_url())

    def test_get_url_defined_in_both_places(self):
        self.options.url = 'url 1'
        os.environ['KANBOARD_URL'] = 'url 2'
        self.assertEqual('url 1', self.client.get_url())

    def test_get_username_not_defined(self):
        self.assertEqual('jsonrpc', self.client.get_username())

    def test_get_username_defined_with_option(self):
        self.options.username = 'some user'
        self.assertEqual('some user', self.client.get_username())

    def test_get_username_defined_with_env_variable(self):
        os.environ['KANBOARD_USERNAME'] = 'another user'
        self.assertEqual('another user', self.client.get_username())

    def test_get_password_not_defined(self):
        with self.assertRaises(exceptions.KanboardException):
            self.client.get_password()

    def test_get_password_defined_with_option(self):
        self.options.password = 'some password'
        self.assertEqual('some password', self.client.get_password())

    def test_get_password_defined_with_env_variable(self):
        os.environ['KANBOARD_PASSWORD'] = 'another password'
        self.assertEqual('another password', self.client.get_password())

    def test_get_auth_header_not_defined(self):
        self.assertEqual('Authorization', self.client.get_auth_header())

    def test_get_auth_header_defined_with_option(self):
        self.options.auth_header = 'some header'
        self.assertEqual('some header', self.client.get_auth_header())

    def test_get_auth_hader_defined_with_env_variable(self):
        os.environ['KANBOARD_AUTH_HEADER'] = 'another header'
        self.assertEqual('another header', self.client.get_auth_header())

    def test_is_super_user(self):
        self.assertTrue(self.client.is_super_user())

        self.options.username = 'admin'
        self.assertFalse(self.client.is_super_user())

    def test_get_client(self):
        self.options.url = 'url'
        self.options.username = 'admin'
        self.options.password = 'secret'
        self.assertIsInstance(self.client.get_client(),
                              kanboard.Kanboard)
