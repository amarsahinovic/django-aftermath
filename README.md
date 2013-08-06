django-aftermath
================

Execute commands after tests are completed.

It requires django-discover-runner package to work. 

Usage
=====

In your settings file, add the following required options:

`TEST_RUNNER = 'aftermath.AftermathTestRunner'`

To specifiy a backend, set a dotted path to the backend class:

`AFTERMATH_BACKEND = 'aftermath.backends.NotifySendBackend'`

Currently, there are two backends, `NullBackend` which does nothing, and `NotifySendBackend` which uses notify-send to generate notifications. You must install notify-send yourself.

On Gnome3, `NotifySendBackend` creates notifications like these:

![notification](notification.png)

To specifiy if backend is executed when all test succeed, use `AFTERMATH_RUN_ON_SUCCESS` setting. Default values is `True`.

To specifiy if backend is executed when some tests fail, use `AFTERMATH_RUN_ON_FAIL` setting. Default values is `True`.

Usually, you will need to specify the first two options. If you wish to implement your own backend, take a look at one of the exisitng backends. All you need is a simple class with `__init__` and `aftermath` functions.

TODO
====

Implement support for Django 1.6 by using builtin test runner, and use django-discover-runner for older versions.
