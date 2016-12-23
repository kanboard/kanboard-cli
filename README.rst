============================
Kanboard Command Line Client
============================

.. image:: https://travis-ci.org/kanboard/kanboard_cli.svg?branch=master
    :target: https://travis-ci.org/kanboard/kanboard_cli

Kanboard command line client.

- Author: Frédéric Guillot
- License: MIT

Installation
============

.. code-block:: bash

    pip install kanboard_cli


This application is compatible with Python 2.7, Python 3.4 and 3.5.

Configuration
=============

You can define connection parameters as environment variables:

.. code-block:: bash

    export KANBOARD_URL=http://localhost/jsonrpc.php
    export KANBOARD_USERNAME=admin
    export KANBOARD_PASSWORD=admin

Or as command line arguments:

.. code-block:: bash

    kanboard --url http://localhost/jsonrpc.php --username admin --password admin

Examples
========

Display application version:

.. code-block:: bash

    kanboard app version
    1.0.35

Display project information:

.. code-block:: bash

    kanboard project show 1
    +-------------+--------------------------------------------------------------------------------+
    | Field       | Value                                                                          |
    +-------------+--------------------------------------------------------------------------------+
    | ID          | 1                                                                              |
    | Name        | Demo Project                                                                   |
    | Description | None                                                                           |
    | Board URL   | http://localhost/?controller=BoardViewController&action=show&project_id=1      |
    +-------------+--------------------------------------------------------------------------------+

