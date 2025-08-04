import pytest
from utilities import helper
from jsonschema import validate
from schemas import search
import json
import logging
from utilities.custom_exceptions import *



@pytest.mark.parametrize("album_search_data",['artist'],indirect=True)
@pytest.mark.usefixture("album_search_data")
class Test_artist:
    def test_artist_limt(self,album_search_data):
        assert isinstance(album_search_data["data"]["artists"]["limit"],int)," limit is not integer"
        assert  isinstance(album_search_data["data"]["artists"]["offset"],int),"offset is not integer"
