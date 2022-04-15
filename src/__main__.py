"""Retrieve docker image tags"""

import argparse
import sys


DESCRIPTION = """\
    List all docker image tags.
    See the README.
"""


def _get_arg_parser():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
    )
    parser.add_argument("image_name", help="docker image name")
    return parser


def main(sys_argv: list = None):
    sys_argv = sys_argv or sys.argv[1:]
    parser = _get_arg_parser()
    args = parser.parse_args(sys_argv)
    return args.image_name
