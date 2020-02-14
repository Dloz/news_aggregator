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
                print("RequestException")
            if response and response.status_code == 200:
                return response.text
            else:
                print("Response failure")
        else:
            pass

    async def fetch_async(self, link):
        if link:
            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(link)
                    return await response.text()
            except ClientError:
                print("ClientError!")
        else:
            raise AttributeError("Link were not provided")
