import argparse

DESCRIPTION = """\
    List all docker image tags.
    See the README.
"""


def get_arg_parser():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
    )
    parser.add_argument("image_name", help="docker image name")
    return parser
