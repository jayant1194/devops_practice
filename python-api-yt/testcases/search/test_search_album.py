import pytest
from utilities import helper
from jsonschema import validate
from schemas import search
import json
import logging
from utilities.custom_exceptions import *
import re 











@pytest.mark.parametrize("album_search_data",['album'],indirect=True)
@pytest.mark.usefixture("album_search_data")
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
            logging.info(["release_date"])
           
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

    def test_album_pagination(self,album_search_data):
      
        for i,j in album_search_data["data"]["albums"].items():
          
            if i=="next":
                assert "offset=" in j 
            if i=="previous":
                assert "offset=" in j
    def test_available_markets(self,album_search_data):
        
        for i in album_search_data["data"]["albums"]["items"]:
            print(len(i["available_markets"]))

    


   
          
    



        
        


    

            

       

    

