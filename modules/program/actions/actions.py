from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
import common as common
import requests


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
    
# liên quan đến chương trình đào tạo
class ActionInformamtionAboutTrainingPrograms(Action): 
    def name(self) -> Text:
        return "action_information_about_training_programs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Xin chào mọi người"

        dispatcher.utter_message(text = message)

        return []

# liên quan đến yêu cầu tuyển sinh
class ActionAdmissionRequirements(Action): 
    def name(self) -> Text:
        return "action_admission_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Xin chào mọi người"
        requirements = requests.get('http://127.0.0.1:5000/program/read/admission_conditions')
        print(requirements.json())

        dispatcher.utter_message(text = message)

        return []

# Liên quan đến chi phí học hành
class ActionTraningCosts(Action): 
    def name(self) -> Text:
        return "action_training_costs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cost = common.SolTrainingCosts('information_technology', data['training_costs'])
        detailCost = common.GetDataFromTrainingCost('information_technology', data['training_costs'])
        
        majorName = 'information_technology'
        studyTime = 10
        studyTimeType: 'tháng'
        costValue = detailCost[0]
        costType = detailCost[1]

        message = "Chi phí của ngành {} trong vòng {} {} sẽ có {} tín chỉ với mới tin chỉ {}. Và tổng chi phí hết là {} ".format(majorName, studyTime, studyTimeType, costValue, costType, cost)
        message = "hello"
        dispatcher.utter_message(text = message)

        return []

# Liên quan đến cơ hội việc làm 
class ActionEmployementOpportunities(Action): 
    def name(self) -> Text:
        return "action_employment_opportunities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        employmentOpportunitiesObj = data.get('employment_opportunities')

        employeeRate = employmentOpportunitiesObj.get('employee_rate')
        jobSearchDurationValue = employmentOpportunitiesObj.get('job_search_duration').get('value')
        jobSearchDurationType = employmentOpportunitiesObj.get('job_search_duration').get('type')
        salaryValue = employmentOpportunitiesObj.get('salary').get('value')
        salaryType = employmentOpportunitiesObj.get('salary').get('type')
        jobSatisfaction = employmentOpportunitiesObj.get('job_satisfaction')

        message = 'Tỉ lệ có việc làm {} sau khi tốt nghiệp với mức lương trung bình {} {} và thời gian trung bình tìm việc làm của sinh viên trung bình  {} {}và tì lệ hài lòng của các doanh nghiệp sau kli sinh viên ra trường đạt {}'.format(
                    employeeRate,
                    jobSearchDurationValue, 
                    jobSearchDurationType, 
                    salaryValue,
                    salaryType, 
                    jobSatisfaction
                )

        dispatcher.utter_message(text = message)

        return []

# liên quan đến các hoạt động của sinh viên   
class ActionStudentActivities(Action): 
    def name(self) -> Text:
        return "action_student_activities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        studentActivitiesObj = data.get('student_activities')

        clubAndStudentOrganizationObj = studentActivitiesObj.get('club_and_student_organization')
        workshopAndEventsObj =  studentActivitiesObj.get('workshop_and_events')
        internshipAndPracticeTrainingObj = studentActivitiesObj.get('internship_and_practice_training')
        scientificResearchObj = studentActivitiesObj.get('scientific_research')

        clubAndStudentOrganizationMes = map(lambda sub: '{}: {}'.format(sub.get('name'), sub.get('description')), clubAndStudentOrganizationObj);
        # workshopAndEventsMes = map(lambda sub: '{}: {}'.format),workshopAndEventsObj)

        studentActivitiesObj = data.get('student_activities')

        clubAndStudentOrganizationObj = studentActivitiesObj.get('club_and_student_organization')
        workshopAndEventsObj =  studentActivitiesObj.get('workshop_and_events')
        internshipAndPracticeTrainingObj = studentActivitiesObj.get('internship_and_practice_training')
        scientificResearchObj = studentActivitiesObj.get('scientific_research')


        clubAndStudentOrganizationIter = map(lambda sub: '{}: {}'.format(sub.get('name'), sub.get('description')), list(clubAndStudentOrganizationObj.values()));

        rows = list(clubAndStudentOrganizationIter)

        message = '\n'.join(rows)

        dispatcher.utter_message(text = message)

        return []

# liên quan đến dịch vụ của sinh viên
class ActionStudentServices(Action): 
    def name(self) -> Text:
        return "action_student_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Xin chào mọi người"

        dispatcher.utter_message(text = message)

        return []
    
# liên quan đến cơ sở vật chất của trường
class ActionFacilities(Action): 
    def name(self) -> Text:
        return "action_facilities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Xin chào mọi người"

        dispatcher.utter_message(text = message)

        return []