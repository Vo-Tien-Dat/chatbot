import json
import requests

def list_courses(json_data, major_name=None): 
    
    data = json_data['data'].values()
    courses = list(filter(lambda course: course['major'] == major_name, list(data)))
    return courses

domain = 'http://127.0.0.1:5000/major/read/courses'
request = requests.get(domain)
json_data = request.json()
courses = list_courses(json_data, 'vi_tinh')
def message_courses(courses): 
    sub_message_course = '{}: {}'
    message = [sub_message_course.format(course['name'], course['semeter']) for course in courses]
    print(message)
    message = ''
    return message


time = {'type': 'month', 'value': 10}

def educational_experience(data): 
    educational_experience_type = {
        'year': 'năm', 
        'month': 'tháng'
    }
    message_pattern = '{} {}'
    message = message_pattern.format(data['value'], educational_experience_type[data['type']])
    return message

print(educational_experience(time))
