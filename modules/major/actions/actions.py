from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
import common as commmon

# ĐỌC DỮ LIỆU TẠM THỜI BẰNG FILE JSON
def read_json(fileName: Text): 
    data = None
    with open(fileName, 'r') as file: 
        data = json.loads(file.read())
    return data

data = read_json('data.json')

# XÂY DỰNG CÁC ACTION DÀNH CHO MỘT TRONG MỘT PHƯƠNG ÁN TUYỂN SINH
class ActionListAllCoursesInMajor(Action):

    def name(self) -> Text:
        return "action_list_all_courses_in_major"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return []
    

class ActionListAllLecturerInMajor(Action):
    def name(self) -> Text:
        return "action_list_all_lecturer_in_major"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return []