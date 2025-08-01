import pytest
from utilities import helper
from jsonschema import validate
from schemas import search
import json
import logging
from utilities.custom_exceptions import *

@pytest.mark.usefixtures("setup")
class Test_search_album():
    #test album with q,type,market,limit,offset,include_external
    def test_search(self,setup):
        token=setup
        resp=helper.get_search(token=token,q="master",type="album",limit=2,offset=1,include_external="audio")
        print(resp)
        print(resp.status_code)
        assert resp.status_code==200, "failure due to not sucess 200 statuscode"
        print(resp)
      
        #validate json schema
        try:
            validate(instance=resp.json(),schema=helper.load_file("schemas/search/test_search_full.json"))
            logging.info("this is success")
        except Exception as e:
            raise JsonschemaException("json schema failed")
        #this is the first testcase
    

            

       

    

