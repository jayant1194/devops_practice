import pytest
from utilities import helper
from jsonschema import validate
from schemas import search
import json
import logging
from utilities.custom_exceptions import *








@pytest.fixture(scope="class")
def album_search_data(setup):
    token=setup
    resp=helper.get_search(token=token,q="master",type="album",limit=2,offset=1,include_external="audio")
    # print(resp)
    print(resp.status_code)
    assert resp.status_code==200, "failure due to not sucess 200 statuscode"
    # print(resp.json())
        
      
        #validate json schema
        try:
            validate(instance=resp.json(),schema=helper.load_file("schemas/search/test_search_full.json"))
            logging.info("this is success")
        except Exception as e:
            raise JsonschemaException("json schema failed")
    return {"data":resp.json()}



@pytest.mark.usefixtures("album_search_data")
class Test_search_album():
   
  
  



  
    #TC01
   
    # def test_album_check(self,album_search_data):
    #     self.data=album_search_data["data"]
    def test_album(self,album_search_data):
        # print(album_search_data)
        assert album_search_data["data"]["albums"]["limit"]==2 ,"this is not expected"
        assert album_search_data["data"]["albums"]["offset"]==1, "offset failure"
        for i in album_search_data["data"]["albums"]["items"]:
            assert i["album_type"]=="album",f"expected album but got {i['album_type']}"
            
        


    

            

       

    

