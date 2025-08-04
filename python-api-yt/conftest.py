import pytest
import requests

from utilities import helper
from jsonschema import validate
from schemas import search
import json
import logging
from utilities.custom_exceptions import *
import re 
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


@pytest.fixture(scope="class")
def album_search_data(request,setup):
    token=setup
    search_type=request.param
    resp=helper.get_search(token=token,q="master",type=search_type,limit=2,offset=1,include_external="audio")
    # print(resp)
    print(resp.status_code)
    assert resp.status_code==200, "failure due to not sucess 200 statuscode"
    # print(resp.json())
        
      
        #validate json schema
    try:
        validate(instance=resp.json(),schema=helper.load_file(f"schemas/search/test_search_{search_type}.json"))
        logging.info("this is success")
    except Exception as e:
        raise JsonschemaException("json schema failed")
    return {"data":resp.json()}




