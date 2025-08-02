import pytest
from utilities import helper
from jsonschema import validate
from schemas import search
import json
import logging
from utilities.custom_exceptions import *
import re 








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
    def test_album_item(self,album_search_data):
        # print(album_search_data)
        assert album_search_data["data"]["albums"]["limit"]==2 ,"this is not expected"
        assert album_search_data["data"]["albums"]["offset"]==1, "offset failure"
        for i in album_search_data["data"]["albums"]["items"]:
            assert i["album_type"]=="album",f"expected album but got {i['album_type']}"
            assert isinstance(i["total_tracks"],int) ,"we didnt get int"
            print(i["release_date"])
           
    #tc02
    def  test_album_itemdate_validation(self,album_search_data):
        date_format=r"\d{4}-(0[0-9]|1[0-2])-(0[1-9]|[12]\d|3[0-1])"
        
        for i in album_search_data["data"]["albums"]["items"]:
            try:
                match=re.fullmatch(date_format,i["release_date"])
                assert bool(match), "expected valid date format , but got invalid"
                logging.info("this is success")
            except AssertionError :
                raise InvaliddateException("we got invalid date format")
            except TypeError:
                raise TypeError("this is not valid form")
    def test_album_artistname(self,album_search_data):
        for i in album_search_data["data"]["albums"]["items"]:
            print(len(i["artists"]))
            for j in i["artists"]:
                print(j["name"])
                assert j["type"]=="artist", "artist is not there"





        
        


    

            

       

    


