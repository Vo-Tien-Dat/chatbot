from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
import common as commmon
import requests
from dotenv import load_dotenv
import os
from underthesea import classify

load_dotenv()
port = os.getenv('PORT')
url = os.getenv('URL')
CONST_DOMAIN = '{}:{}'.format(url,port)



def check_existing_major(major_name): 
    CONST_MAJOR = ['vi_tinh', 'kinh_doanh', 'phap_luat']
    if major_name in CONST_MAJOR:
        return True
    return False

def list_courses(json_data, major_name=None): 
    
    data = json_data['data'].values()
    courses = list(filter(lambda course: course['major'] == major_name, list(data)))    
    return courses

def message_courses(courses): 
    if(len(courses) == 0): 
        return "Không có môn học nào cả"
    sub_message_course = '{}'
    message = '\n'.join([sub_message_course.format(course['name']) for course in courses])
    return message

def list_lecturer(json_data, major_name): 
    data = json_data['data'].values()
    lecturers = list(filter(lambda lecturer: major_name in lecturer['major'] , list(data))) 
    return lecturers

def educational_experience(data): 
    educational_experience_type = {
        'year': 'năm', 
        'month': 'tháng'
    }
    message_pattern = '{} {}'
    message = message_pattern.format(data['value'], educational_experience_type[data['type']])
    return message

def message_lecturer(lecturers): 
    if(len(lecturers) == 0): 
        return "Không có giáo viên nào"
    sub_message = 'Tên giáo viên: {} \n Số năm kinh nghiêm: {}'
    message = '\n'.join([sub_message.format(lecturer['name'],educational_experience(lecturer['educational_experience'])) for lecturer in lecturers])
    return message

# XÂY DỰNG CÁC ACTION DÀNH CHO MỘT TRONG MỘT PHƯƠNG ÁN TUYỂN SINH
class ActionListAllCoursesInMajor(Action):

    def name(self) -> Text:
        return "action_list_all_courses_in_major"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        domain = CONST_DOMAIN + '/major/read/courses'
        request = requests.get(domain)
        
        slot_major_value = tracker.get_slot("major")
        classify_major_value = classify(slot_major_value)

        try: 
            major_name = classify_major_value[0]
            print(major_name)
            if check_existing_major(major_name=major_name) == False:
                raise ValueError("Chúng tôi không có mảng này")
            
            if request.status_code == 200: 
                courses = list_courses(request.json(),major_name=major_name)
                message = message_courses(courses=courses)
            
            if request.status_code == 500: 
                raise ValueError('Error Server')
            
        except Exception as e: 
            message = str(e)

        dispatcher.utter_message(text=message)
        return []
    
# XÂY DỰNG DÀNH ĐỂ TÌM GIÁO VIÊN HỖ TRỢ GIẢNG DẠY 
class ActionListAllLecturerInMajor(Action):
    def name(self) -> Text:
        return "action_list_all_lecturer_in_major"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        domain = CONST_DOMAIN + '/major/read/lecturer'
        request = requests.get(domain)

        slot_major_value = tracker.get_slot("major")
        classify_major_value = classify(slot_major_value)

        try: 
            major_name = classify_major_value[0]
            if check_existing_major(major_name=major_name) == False:
                raise ValueError("Chúng tôi không có mảng này")
            
            if request.status_code == 200: 
                lecturers = list_lecturer(request.json(),major_name=major_name)
            
                message = message_lecturer(lecturers)
            
            if request.status_code == 500: 
                raise ValueError('Error Server')
            
        except Exception as e: 
            message = str(e)

        dispatcher.utter_message(text=message)
        return []