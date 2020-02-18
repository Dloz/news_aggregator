import logging

import aiohttp
import requests
from aiohttp import ClientError
from requests import RequestException


class HTTPFetcher:

    def fetch(self, link):
        if link:
            response = None
            try:
                response = requests.get(link)
            except RequestException:
                logging.exception(f"{link} request exception")
            if response and response.status_code == 200:
                return response.text
            else:
                logging.exception(f"Response from {link} failure")
        else:
            raise ValueError("Link were not provided")

    async def fetch_async(self, link):
        if link:
            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(link)
                    return await response.text()
            except ClientError:
                logging.exception(f"ClientError at {link}")
        else:
            raise ValueError("Link were not provided")
