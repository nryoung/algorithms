#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import subprocess
import sys

import pytest


FLAKE8_ARGS = ['algorithms']

sys.path.append(os.path.dirname(__file__))


def exit_on_failure(ret, message=None):
    if ret:
        sys.exit(ret)


def flake8_main(args):
    print('Running flake8 code linting')
    ret = subprocess.call(['flake8'] + args)
    print('flake8 failed' if ret else 'flake8 passed')
    return ret


if __name__ == '__main__':
    run_tests = True
    run_flake8 = True

    try:
        sys.argv.remove('--lintonly')
    except ValueError:
        run_tests = True
    else:
        run_tests = False
        run_flake8 = True

    if run_tests:
        exit_on_failure(pytest.main())

    if run_flake8:
        exit_on_failure(flake8_main(FLAKE8_ARGS))
