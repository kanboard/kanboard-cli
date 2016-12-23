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

from cliff import app
from cliff import commandmanager
from pbr import version as app_version
import sys

from kanboard_cli.commands import application
from kanboard_cli.commands import project
from kanboard_cli.commands import task
from kanboard_cli import client


class KanboardShell(app.App):

    def __init__(self):
        super(KanboardShell, self).__init__(
            description='Kanboard Command Line Client',
            version=app_version.VersionInfo('kanboard_cli').version_string(),
            command_manager=commandmanager.CommandManager('kanboard.cli'),
            deferred_help=True)
        self.client = None
        self.is_super_user = True

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super(KanboardShell, self).build_option_parser(
            description, version, argparse_kwargs=argparse_kwargs)

        parser.add_argument(
            '--url',
            metavar='<api url>',
            help='Kanboard API URL',
        )

        parser.add_argument(
            '--username',
            metavar='<api username>',
            help='API username',
        )

        parser.add_argument(
            '--password',
            metavar='<api password>',
            help='API password/token',
        )

        parser.add_argument(
            '--auth-header',
            metavar='<authentication header>',
            help='API authentication header',
        )

        return parser

    def initialize_app(self, argv):
        client_manager = client.ClientManager(self.options)
        self.client = client_manager.get_client()
        self.is_super_user = client_manager.is_super_user()

        self.command_manager.add_command('app version', application.ShowVersion)
        self.command_manager.add_command('app timezone', application.ShowTimezone)
        self.command_manager.add_command('project show', project.ShowProject)
        self.command_manager.add_command('project list', project.ListProjects)
        self.command_manager.add_command('task create', task.CreateTask)
        self.command_manager.add_command('task list', task.ListTasks)


def main(argv=sys.argv[1:]):
    return KanboardShell().run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
