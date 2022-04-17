import json
import random
import ssl
import time
import urllib.request
from http import HTTPStatus

from .logger import logger


class NotExpectedResponseStatus(Exception):
    pass


def fetch_json_from_url(url: str) -> dict:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    expected_resp_status = HTTPStatus.OK

    print(f"fetching from {url}")

    with urllib.request.urlopen(url, context=ctx) as response:
        resp = response.read()
        if response.status == expected_resp_status:
            return json.loads(resp)
        logger.debug(resp)
        raise NotExpectedResponseStatus(
            message=f"Expected {expected_resp_status} Got {response.status}"
        )


def random_sleep():
    sleep_time = round(random.uniform(0, 3), 2)
    time.sleep(sleep_time)
