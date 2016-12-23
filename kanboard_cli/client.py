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
import os

from kanboard_cli import exceptions


class ClientManager(object):

    def __init__(self, options):
        self.options = options

    def get_client(self):
        return kanboard.Kanboard(url=self.get_url(),
                                 username=self.get_username(),
                                 password=self.get_password(),
                                 auth_header=self.get_auth_header())

    def is_super_user(self):
        return self.get_username() == 'jsonrpc'

    def get_url(self):
        return self._get_option('url', error_message='API URL is required')

    def get_username(self):
        return self._get_option('username', default='jsonrpc')

    def get_password(self):
        return self._get_option('password', error_message='API password is required')

    def get_auth_header(self):
        return self._get_option('auth_header', default='Authorization')

    def _get_option(self, name, default=None, error_message=None):
        env_variable = 'KANBOARD_' + name.upper()
        value = getattr(self.options, name)

        if value:
            return value
        elif env_variable in os.environ:
            return os.environ[env_variable]
        elif default is None:
            raise exceptions.KanboardException(error_message)
        return default
