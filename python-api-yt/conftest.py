import pytest
import requests

import json


class testing:
    def __init__(self):
        self.client_id="f092eefd6d80496c836738dc9b75aefc"
        self.client_secret="83d23b636eb04d6a8f792fdfca5db9b9"
        self.headers={
            "Content-Type": "application/x-www-form-urlencoded" 
        }
        # self.access_token=""
        self.url="https://accounts.spotify.com/api/token"
        self.payload={
            "grant_type":"client_credentials",
            "client_id":self.client_id,
            "client_secret":self.client_secret
            }
        self.token=""

    def get_token(self):
        response=requests.post(self.url,headers=self.headers,data=self.payload)
        data=response.json()
        print(response.json())
        self.token=data["access_token"]
        return self.token 

@pytest.fixture(scope="session")   
def setup():
    return testing().get_token()





