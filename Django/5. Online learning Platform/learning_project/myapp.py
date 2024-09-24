import json
import requests
import datetime
    
# my_model = MyModel()
# my_model.duration = datetime.timedelta(days=20, hours=10)

URL = 'http://127.0.0.1:8000/course-create/'

data = {
    "course_id": 104,
    "title": "Mathematics",
    "description": "Learning angles to dodge",
    "instructor": "12kdna12",
    'duration': str(datetime.timedelta(seconds=15000)),
    }

print('Data = ', data)
json_data = json.dumps(data)


r = requests.post(url=URL, data=json_data)

data1 = r.json
print(data1)

# URL = 'http://127.0.0.1:8000/student-create/'

# data = {
#     'rollNo': 102,
#     'name': 'Bilal Yusuf',
#     'city': 'Quetta',
# }

# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data1 = r.json
# print('data1 : ', data1)


# URL = 'http://127.0.0.1:8000/student-update/102'

# data = {
#     'city': 'karachi',
# }

# json_data = json.dumps(data)
# r = requests.put(url=URL, data=json_data)
# data1 = r.json
# print('data1 : ', data1)
