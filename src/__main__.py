"""Retrieve all docker image tags"""

import sys
from typing import List

from .arg_parser import get_arg_parser
from .utils import fetch_json_from_url, random_sleep

API_BASE_URL = "https://registry.hub.docker.com/v2/repositories"


def filter_tags(arr):
    result = []
    for image in arr:
        result.append(image["name"])
    return result


def fetch_repo_tags(image_name: str) -> List[str]:
    tags = []

    if "/" in image_name:
        next_url = f"{API_BASE_URL}/{image_name}/tags"
    else:
        next_url = f"{API_BASE_URL}/library/{image_name}/tags"

    while next_url:
        response = fetch_json_from_url(next_url)
        tags += filter_tags(response.get("results", []))
        next_url = response.get("next")
        random_sleep()

    return tags


def main(sys_argv: list = None):
    sys_argv = sys_argv or sys.argv[1:]

    parser = get_arg_parser()
    args = parser.parse_args(sys_argv)

    tags = fetch_repo_tags(args.image_name)

    for t in tags:
        print(f"{args.image_name}:{t}")
