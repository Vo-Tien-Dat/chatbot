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
class ActionAdmission(Action):

    def name(self) -> Text:
        return "action_admission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rows = []
        values = data['admission_conditions'].values()
        index = 1

        for value in values: 
            rows.append("{}:{}".format(index, value['description']))
            index = index + 1
        message = '' if len(rows) == 0 else '\n' .join(rows)

        dispatcher.utter_message(text=message)
        return []
    
class ActionAdmissionMethod(Action):  

    def name(self) -> Text:
        return "action_admission_method"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        rows = []
        values = data['admission_method'].values()
        
        # lấy thông tin về các phương thức tuyển sinh và mô tả
        for value in values: 
            rows.append("{}:{}".format(value['name'], value['description']))
        message = '' if len(rows) == 0 else '\n' .join(rows)
    
        dispatcher.utter_message(text=message)

        return []
    
class ActionRegisterTime(Action): 
    def name(self) -> Text:
        return "action_register_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dateOfAdmission = data['date_of_admission']
        dateOfAdmissionObj = date_obj = datetime.strptime(dateOfAdmission, "%d-%m-%Y %H:%M:%S")
        message = "Thời gian để đăng ký việc nhập học cua trường vào ngày {} tháng {} năm {} vào lúc {} giờ".format(dateOfAdmissionObj.day, dateOfAdmissionObj.month, dateOfAdmissionObj.year, dateOfAdmissionObj.hour, dateOfAdmissionObj.minute)

        dispatcher.utter_message(text = message)

        return []


class ActionGreet(Action): 
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Xin chào mọi người"

        dispatcher.utter_message(text = message)

        return []