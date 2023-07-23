from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime


# ĐỌC DỮ LIỆU TẠM THỜI BẰNG FILE JSON
def read_json(fileName: Text): 
    data = None
    with open(fileName, 'r') as file: 
        data = json.loads(file.read())
    return data

data = read_json('data.json')

# XÂY DỰNG CÁC ACTION DÀNH CHO MỘT TRONG MỘT PHƯƠNG ÁN TUYỂN SINH
class ActionListOfScholarship(Action):

    def name(self) -> Text:
        return "action_list_of_scholarships"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        rows = []
        values = data['scholarship'].values()
        index = 1

        for value in values: 
            rows.append("{}. {}: {}".format(index, value['name'], value['description']))
            index = index + 1
        message = '' if len(rows) == 0 else '\n' .join(rows)

        dispatcher.utter_message(text=message)
        return []
    
class ActionDetailScholarship(Action):

    def name(self) -> Text:
        return "action_detail_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = ''

        dispatcher.utter_message(text=message)
        return []
