
import pytest
import requests
import json
import logging


def get_search(**kwargs):
    token=kwargs.get("token")
    if not token:
        raise ValueError("token is missing")

    headers={
        "Authorization": f"Bearer {token}"
    }
    url="https://api.spotify.com/v1/search"
    params={}
    
    if "q" in kwargs:
        params["q"]=kwargs["q"]
    if "type" in kwargs:
        params["type"]=kwargs["type"]
    if "limit" in kwargs:
        params["limit"]=kwargs["limit"]
    if "offset" in kwargs:
        params["offset"]=kwargs["offset"]
    if "include_external" in kwargs:
        params["include_external"]=kwargs["include_external"]
   
    response=requests.get(url,params=params,headers=headers)
    return response


# curl --request GET \
#   --url 'https://api.spotify.com/v1/search?q=master&type=artist&limit=4&offset=1&include_external=audio' \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'


def load_file(filename):
    with open(filename,"r") as f:
        return json.load(f)

# def loggers():
#     logging.
